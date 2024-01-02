from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .views import *

urlpatterns = [
    path('rooms/', views.rooms),
    path('rooms/<int:room_id>', views.room_detail),
    path('floors/', views.get_floors),
    path('free_rooms/<str:check_in_date>/<str:check_out_date>/', views.check_availability, name='check_availability'),
    path('quarterly_report/<int:quarter>/<int:year>/', views.quarterly_report, name='quarterly_report'),
    path('all_bookings/', views.all_bookings, name='all_bookings'),
    path('all_bookings/<int:booking_id>/', views.update_check_in_out),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]