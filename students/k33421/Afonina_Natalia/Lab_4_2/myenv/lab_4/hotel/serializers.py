from rest_framework import routers, serializers, viewsets
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'


class RoomClientReportSerializer(serializers.Serializer):
    room__number = serializers.CharField()
    num_clients = serializers.IntegerField()


class FloorReportSerializer(serializers.Serializer):
    floor = serializers.IntegerField()
    num_rooms = serializers.IntegerField()


class TotalIncomeForRoomSerializer(serializers.Serializer):
    room__number = serializers.CharField()
    total_income_for_room = serializers.IntegerField()


class HotelReportSerializer(serializers.Serializer):
    room_client_reports = RoomClientReportSerializer(many=True)
    floor_reports = FloorReportSerializer(many=True)
    total_income_for_room = TotalIncomeForRoomSerializer(many=True)
    total_income_for_hotel = serializers.IntegerField()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
