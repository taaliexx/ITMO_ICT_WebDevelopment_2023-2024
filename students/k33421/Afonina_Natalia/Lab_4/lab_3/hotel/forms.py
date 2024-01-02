from django import forms


class ClientsFromCityForm(forms.Form):
    city = forms.CharField(max_length=100, required=False)
