from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs.get('check_in') > attrs.get('check_out'):
            raise serializers.ValidationError("Check in date must be before check out")
        return attrs
    
    class Meta:
        model = Reservation
        fields = (
            "id",
            "id_ad",
            "code",
            "guest_amount",
            "total_price",
            "comment",
            "check_in",
            "check_out",
            "created_at",
            "updated_at"
        )