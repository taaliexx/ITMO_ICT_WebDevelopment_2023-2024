from django import forms
from .models import CarOwner, Car


class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ['username', 'password', 'first_name', 'last_name', 'birth_date',
                  'passport', 'address', 'nationality']


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['license_plate', 'car_brand', 'car_model', 'color']


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['license_plate', 'car_brand', 'car_model', 'color']


class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = []
