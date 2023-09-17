from rest_framework import serializers
from realties.models import Realties

class RealtiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realties
        fields = (
            "id",
            "guest_limit",
            "bath_amount",
            "pets_allowed",
            "cleaning_fee",
            "activated_at",
            "created_at",
            "updated_at",
            "active"
        )