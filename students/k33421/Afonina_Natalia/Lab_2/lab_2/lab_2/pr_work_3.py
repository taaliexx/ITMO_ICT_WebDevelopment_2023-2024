from hotel.models import Hotel, Room, CustomUser, Bookings, Review, Confirmation

natashashotel = Hotel.objects.get(id=1)

deluxe_room_4 = Room.objects.create(number=115, category='DELUXE', beds=1, capacity=2, cost=250, amenities='Wi-Fi, Breakfast', hotel=natashashotel)
double_room_3 = Room.objects.create(number=116, category='DOUBLE', beds=1, capacity=2, cost=200, amenities='Wi-Fi, Breakfast', hotel=natashashotel)
single_room_5 = Room.objects.create(number=117, category='SINGLE', beds=1, capacity=1, cost=100, amenities='Wi-Fi, Breakfast', hotel=natashashotel)
single_room_6 = Room.objects.create(number=118, category='SINGLE', beds=1, capacity=1, cost=100, amenities='Wi-Fi, Breakfast', hotel=natashashotel)
family_room_3 = Room.objects.create(number=119, category='FAMILY', beds=3, capacity=4, cost=300, amenities='Wi-Fi, Breakfast', hotel=natashashotel)
suite_4 = Room.objects.create(number=120, category='SUITE', beds=1, capacity=2, cost=400, amenities='Wi-Fi, Breakfast, Lounge access', hotel=natashashotel)
suite_5 = Room.objects.create(number=121, category='SUITE', beds=1, capacity=2, cost=400, amenities='Wi-Fi, Breakfast, Lounge access', hotel=natashashotel)


user_polilaa = CustomUser.objects.get(id=10)
user_natal = CustomUser.objects.get(id=1)


booking_user_polilaa_1 = Bookings.objects.create(user=user_polilaa, room=single_room_5, check_in='2023-11-25', check_out='2023-11-26')
booking_user_polilaa_2 = Bookings.objects.create(user=user_polilaa, room=double_room_3, check_in='2023-11-24 16:00:00', check_out='2023-11-26 16:00:00')
booking_user_natal_1 = Bookings.objects.create(user=user_natal, room=family_room_3, check_in='2023-12-01', check_out='2023-12-05')
booking_user_polilaa_3 = Bookings.objects.create(user=user_polilaa, room=suite_4, check_in='2023-11-24 16:00:00', check_out='2023-11-26 16:00:00')


confirmation_1_polilaa = Confirmation.objects.create(booking=booking_user_polilaa_1, is_confirmed=True, confirmed_by=user_natal)
confirmation_2_polilaa = Confirmation.objects.create(booking=booking_user_polilaa_3, is_confirmed=True, confirmed_by=user_natal)
confirmation_1_natal = Confirmation.objects.create(booking=booking_user_natal_1, is_confirmed=True, confirmed_by=user_natal)

review_1 = Review.objects.create(user=user_polilaa, rating=9, text="Great room!", room=single_room_5, booking=booking_user_polilaa_1)
review_2 = Review.objects.create(user=user_polilaa, rating=10, text="Excellent service!", room=suite_4, booking=booking_user_polilaa_3)
review_3 = Review.objects.create(user=user_natal, rating=8, text="Good experience!", room=family_room_3, booking=booking_user_natal_1)


