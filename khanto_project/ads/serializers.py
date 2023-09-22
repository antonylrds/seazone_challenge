from rest_framework import serializers
from .models import Ads

class AdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = (
            "id",
            "realty_id",
            "platform_origin",
            "platform_fee",
            "created_at",
            "updated_at",
        )
