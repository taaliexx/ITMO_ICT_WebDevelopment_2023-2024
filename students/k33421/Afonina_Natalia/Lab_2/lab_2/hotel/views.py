from allauth.account.views import LoginView, SignupView
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, FormView, View, DeleteView, UpdateView
from .models import Room, Bookings, Review, Confirmation, Hotel
from .forms import AvailabilityForm, EditBookingForm, ReviewForm
from hotel.booking_functions.availability import check_availability
from hotel.booking_functions.get_room_cat_url_list import get_room_cat_url_list


def RoomListView(request):
    room_category_url_list = get_room_cat_url_list()

    context = {
        "room_list": get_room_cat_url_list
    }
    return render(request, 'room_list_view.html', context)


class BookingsListView(ListView):
    model = Bookings

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Bookings.objects.all()
            return booking_list
        else:
            booking_list = Bookings.objects.filter(user=self.request.user)
            return booking_list


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)
        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)
            context = {
                'room_category': room_category,
                'form': form,
                'room_amenities': room.amenities,
                'room_price': room.cost
            }
            return render(request, 'room_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            available_rooms = []
            for room in room_list:
                if check_availability(room, data['check_in'], data['check_out']):
                    if data['check_in'] < data['check_out']:
                        if data['check_in'] > timezone.now():
                            available_rooms.append(room)
                        else:
                            messages.error(request, "You can't book a room for dates in the past.")
                            return redirect('hotel:RoomListView')
                    else:
                        messages.error(request, "You can't book a room with check out earlier than check in.")
                        return redirect('hotel:RoomListView')
                else:
                    messages.error(request, "Room is fully booked for the selected dates.")
                    return redirect('hotel:RoomListView')
            if len(available_rooms) > 0:
                room = available_rooms[0]
                booking = Bookings.objects.create(
                    user=self.request.user,
                    room=room,
                    check_in=data['check_in'],
                    check_out=data['check_out']
                )
                booking.save()
                confirmation = Confirmation.objects.create(
                    booking=booking,
                    is_confirmed=False,
                    confirmed_by=None
                )
                confirmation.save()
                messages.success(request, 'Your booking created')
                return redirect('hotel:RoomListView')
            else:
                messages.error(request, 'This category of rooms is fully booked. Try another one')
                return redirect('hotel:RoomListView')


class CancelBookingView(DeleteView):
    model = Bookings
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('hotel:BookingsListView')


class EditBookingView(UpdateView):
    model = Bookings
    form_class = EditBookingForm
    template_name = 'edit_booking.html'
    success_url = reverse_lazy('hotel:BookingsListView')

    def form_valid(self, form):
        if form.has_changed():
            data = form.cleaned_data
            room = data['room']
            if check_availability(room, data['check_in'], data['check_out']):
                if data['check_in'] > timezone.now():
                    form.save()
                    messages.success(self.request, 'Your booking has been updated')
                    return redirect(self.success_url)
                else:
                    messages.error(self.request, "You can't book a room for dates in the past.")
                    return redirect('hotel:BookingsListView')
            else:
                messages.error(self.request, 'This room is fully booked for the selected dates. Try another one')
                return redirect('hotel:BookingsListView')
        else:
            messages.info(self.request, 'No changes were made')
            return redirect('hotel:BookingsListView')


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'hotel/review_list.html', {'reviews': reviews})


class AddReviewView(View):
    template_name = 'hotel/add_review.html'

    def get(self, request):
        form = ReviewForm()
        if self.request.user.is_staff:
            return render(request, self.template_name, {'form': form})
        else:
            bookings = Bookings.objects.filter(user=self.request.user, confirmation__is_confirmed=True)
            form.fields['booking'].queryset = bookings
            room_ids = [booking.room.id for booking in bookings]
            form.fields['room'].queryset = Room.objects.filter(id__in=room_ids)

            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)
        user = self.request.user

        if form.is_valid():
            booking_id = form.cleaned_data['booking'].id
            room_id = form.cleaned_data['room'].id
            rating = form.cleaned_data['rating']
            text = form.cleaned_data['text']

            if user.is_staff:
                review = Review.objects.create(user=user, booking_id=booking_id, room_id=room_id, rating=rating,
                                               text=text)
                review.save()
            else:
                bookings = Bookings.objects.filter(user=user)
                form.fields['booking'].queryset = bookings
                room_ids = [booking.room.id for booking in bookings]
                form.fields['room'].queryset = Room.objects.filter(id__in=room_ids)

                # Check if the form is valid again after updating querysets
                if form.is_valid():
                    review = Review.objects.create(user=user, booking_id=booking_id, room_id=room_id, rating=rating,
                                                   text=text)
                    review.save()
            return redirect('hotel:review_list')
        else:
            return redirect('hotel:review_list')


def IndexView(request):
    hotel_info = Hotel.objects.first()
    context = {
        "hotel_info": hotel_info
    }
    return render(request, 'index.html', context)


def HomeView(request):
    return render(request, 'home.html')
