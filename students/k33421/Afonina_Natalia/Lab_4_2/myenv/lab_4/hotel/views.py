import json
from json import JSONDecodeError

from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import *
from .models import *
from django.http import JsonResponse
from .utils import get_available_rooms
from django.db.models import Count, Sum, ExpressionWrapper, F, fields, Expression
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import make_aware
from datetime import datetime
from django.contrib.auth.decorators import login_required


@csrf_exempt
def rooms(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def room_detail(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
        except JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        serializer = RoomSerializer(room, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        room.delete()
        # return a no content response.
        return HttpResponse(status=204)


@csrf_exempt
def get_floors(request):
    if request.method == 'GET':
        floors = Floor.objects.all()
        serializer = FloorSerializer(floors, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FloorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def check_availability(request, check_in_date, check_out_date):
    if request.method == 'GET':
        try:
            # Проверка доступности комнат для указанных дат
            available_rooms = get_available_rooms(check_in_date, check_out_date)

            return JsonResponse(list(available_rooms.values()), safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def quarterly_report(request, quarter, year):
    if request.method == 'GET':
        try:
            start_date = f'{year}-{(quarter - 1) * 3 + 1}-01'
            end_date = f'{year}-{quarter * 3}-01'

            room_client_reports = Bookings.objects.filter(
                check_in__gte=start_date
            ).values('room__number').annotate(
                num_clients=Count('user')
            )

            floor_reports = Room.objects.values('floor').annotate(
                num_rooms=Count('id')
            )

            total_income_room = Bookings.objects.filter(
                check_in__gte=start_date
            ).values('room__number').annotate(
                total_income_for_room=Sum('room__cost')
            )

            total_income_hotel = Bookings.objects.filter(
                check_in__gte=start_date
            ).values('room__number').annotate(
                total_income_hotel=Coalesce(Sum('room__cost'), 0)
            ).aggregate(
                total_income_for_hotel=Sum('total_income_hotel')
            )['total_income_for_hotel']

            serializer = HotelReportSerializer({
                'room_client_reports': room_client_reports,
                'floor_reports': floor_reports,
                'total_income_for_room': total_income_room,
                'total_income_for_hotel': total_income_hotel,
            })

            return JsonResponse(serializer.data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def all_bookings(request):
    if request.method == 'GET':
        bookings = Bookings.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
@require_http_methods(["PATCH"])
def update_check_in_out(request, booking_id):
    try:
        booking = get_object_or_404(Bookings, pk=booking_id)
        data = json.loads(request.body.decode('utf-8'))
        update_type = data.get('update_type')

        if update_type == 'check_in':
            booking.check_in_done = not booking.check_in_done
        elif update_type == 'check_out':
            booking.check_out_done = not booking.check_out_done

        booking.save()

        # Возвращаем обновленные данные
        serializer = BookingSerializer(booking)
        return JsonResponse(serializer.data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)