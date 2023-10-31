```python title="urls.py"
from django.urls import path
from .views import RoomListView, BookingsListView, RoomDetailView, CancelBookingView, EditBookingView, IndexView
from . import views
from allauth.account.views import LoginView, LogoutView, SignupForm

app_name = 'hotel'

urlpatterns = [
    path('', views.IndexView, name='IndexView'),
    path('room_list/', views.RoomListView, name='RoomListView'),
    path('bookings_list/', views.BookingsListView.as_view(), name='BookingsListView'),
    path('room/<category>', views.RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', views.CancelBookingView.as_view(), name='CancelBookingView'),
    path('edit_booking/<pk>/', views.EditBookingView.as_view(), name='EditBookingView'),
    path('reviews/', views.review_list, name='review_list'),
    path('add_review/', views.AddReviewView.as_view(), name='add_review'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    path('home/', views.HomeView, name='HomeView')
]
```