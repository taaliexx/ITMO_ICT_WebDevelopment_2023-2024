from datetime import datetime

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import *
from .serializers import *
from django.shortcuts import render


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class ClientListAPIView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class EmployeeListAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class RoomCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# class RoomCreateView(APIView):
#     def get(self, request):
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = RoomCreateSerializer(data=request.data)
#
#         if serializer.is_valid(raise_exception=True):
#             room_saved = serializer.save()
#             return Response({"Success": "Room '{}' created successfully.".format(room_saved.number)})
#         else:
#             return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def clients_in_room_form(request):
    return render(request, 'clients_in_room_form.html')


class ClientsInRoomView(APIView):
    def get(self, request, room_number, start_date, end_date):
        try:
            bookings = Bookings.objects.filter(
                room__number=room_number,
                check_in__range=[start_date, end_date],
                check_out__range=[start_date, end_date]
            )
            serializer = BookingSerializer(bookings, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def clients_from_city_form(request):
    return render(request, 'clients_from_city_form.html')


class ClientsFromCityView(APIView):
    def get(self, request, city):
        try:
            clients = Client.objects.filter(from_city=city)
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def cleaner_for_client_form(request):
    clients = Client.objects.all()
    return render(request, 'cleaner_for_client_form.html', {'clients': clients})


class CleanerInfoView(APIView):
    def get(self, request, client_id, work_day):
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return Response({"error": f"Client with id {client_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        schedules = RoomCleaningSchedule.objects.filter(
            room__bookings__user=client,
            work_date__week_day=work_day
        )

        serializer = EmployeeScheduleSerializer(schedules, many=True)
        return Response(serializer.data)


def free_rooms_for_date(request):
    return render(request, 'free_room_for_date.html')


class FreeRoomsAPIView(APIView):
    def get(self, request, check_in_date, check_out_date):
        try:
            check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d').date()
            check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d').date()

            all_rooms = Room.objects.all()

            booked_rooms = Bookings.objects.filter(
                check_in__lte=check_out_date,
                check_out__gte=check_in_date
            ).values_list('room_id', flat=True)

            free_rooms = all_rooms.exclude(id__in=booked_rooms)

            serializer = RoomSerializer(free_rooms, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def clients_in_the_same_days(request):
    clients = Client.objects.all()
    return render(request, 'clients_in_same_days_form.html', {'clients': clients})


from django.db.models import Q


class ClientsInSameDaysView(APIView):
    def get(self, request, client_id, check_in_date, check_out_date):
        try:

            other_clients = Client.objects.exclude(id=client_id)

            bookings_in_same_days = Bookings.objects.filter(
                user__in=other_clients,
                check_in__lte=check_out_date,
                check_in__gte=check_in_date
            )

            serializer = BookingSerializer(bookings_in_same_days, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
