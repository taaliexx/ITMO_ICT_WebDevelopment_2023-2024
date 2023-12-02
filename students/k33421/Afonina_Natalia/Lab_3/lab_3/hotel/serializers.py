from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'


class EmployeeScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSchedule
        fields = '__all__'


class CheckInClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ["check_in_done", "check_out_done"]


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