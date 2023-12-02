from django.urls import path, include, re_path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


app_name = "hotel"

urlpatterns = [
    path('rooms/', RoomListAPIView.as_view(), name='room_list'),
    path('clients/', ClientListAPIView.as_view(), name='client_list'),
    path('employees/', EmployeeListAPIView.as_view(), name='employee_list'),
    path('create_room/', RoomCreateView.as_view(), name='create_room'),
    path('clients_in_room/<int:room_number>/<start_date>/<end_date>/', ClientsInRoomView.as_view(),
         name='clients_in_room'),
    path('clients_in_room_form/', clients_in_room_form, name='clients_in_room_form'),
    path('clients_from_city/<str:city>/', ClientsFromCityView.as_view(), name='clients_from_city'),
    path('clients_from_city_form/', clients_from_city_form, name='clients_from_city_form'),
    path('cleaner_for_client_form/', cleaner_for_client_form, name='cleaner_for_client_form'),
    path('cleaner_info/<int:client_id>/<int:work_day>/', CleanerInfoView.as_view(), name='cleaner_info'),
    path('free_rooms_form/', free_rooms_for_date, name='cleaner_for_client_form'),
    path('free_rooms/<str:check_in_date>/<str:check_out_date>/', FreeRoomsAPIView.as_view(), name='free_rooms'),
    path('clients_in_the_same_days_form/', clients_in_the_same_days, name='clients_in_the_same_days'),
    path('clients_in_same_days/<int:client_id>/<str:check_in_date>/<str:check_out_date>/',
         ClientsInSameDaysView.as_view(), name='clients_in_same_days'),
    path('v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]