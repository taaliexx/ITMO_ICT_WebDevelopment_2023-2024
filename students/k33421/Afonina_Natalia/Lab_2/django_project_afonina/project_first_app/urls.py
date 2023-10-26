from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('owner/<int:owner_id>/', views.owner_detail),
    path('time/', views.example_view),
    path('owners/', views.owners_view, name='owners'),
    path('car_list/', views.CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', views.CarDetailView.as_view()),
    path('owners/create/', views.car_owner_create, name='car_owner_create'),
    path('car/create/', views.CarCreateView.as_view(), name='car_create'),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),
]