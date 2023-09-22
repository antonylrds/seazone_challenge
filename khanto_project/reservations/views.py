from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationListView(APIView):
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class ReservationDetailView(APIView):
    def get(self, request, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        if not reservation:
            return Response({"res": "Reservation not found"}, status=HTTP_404_NOT_FOUND)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def delete(self, request, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        if not reservation:
            return Response({"res": "Reservation not found"}, status=HTTP_404_NOT_FOUND)
        reservation.delete()
        return Response({"res": "Reservation deleted."}, status=HTTP_200_OK)