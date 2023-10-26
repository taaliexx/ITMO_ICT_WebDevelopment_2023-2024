from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import CarOwner, Car, DriversLicense, Ownership
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import CarOwnerForm, CarCreateForm, CarUpdateForm, CarDeleteForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def owner_detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except ObjectDoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'owner': owner})


def example_view(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)


def owners_view(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, 'owners_view.html', context)


def car_owner_create(request):
    context = {}

    form = CarOwnerForm(request.POST or None)
    # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
        return redirect('owners')
    context['form'] = form
    return render(request, "car_owner_create.html", context)


class CarListView(ListView):
    model = Car
    queryset = model.objects.all()
    template_name = 'car_list.html'

    def get_queryset(self):
        car = self.request.GET.get('car')

        if car:

            try:
                car = int(car)
                queryset = self.queryset.filter(car=car)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_update.html'
    form_class = CarUpdateForm
    success_url = reverse_lazy('car_list')


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_create.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('car_list')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    form_class = CarDeleteForm
    success_url = reverse_lazy('car_list')


def index(request):
    return render(request, 'index.html')