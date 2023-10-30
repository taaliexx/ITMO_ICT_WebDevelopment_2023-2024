from allauth.account.forms import SignupForm
from django import forms

from hotel.models import Bookings, Review, Room


class AvailabilityForm(forms.Form):
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])


class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['room', 'check_in', 'check_out']


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'text', 'room', 'booking']
