from django.db import models
from realties.models import Realties

# Create your models here.
class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    realty_id = models.ForeignKey(Realties, on_delete=models.CASCADE)
    platform_origin = models.CharField(max_length=200)
    platform_fee = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
