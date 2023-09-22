from django.db import models
from ads.models import Ads
from django.core.exceptions import ValidationError
from .utils import generate_random_string

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    id_ad = models.ForeignKey(Ads, on_delete=models.CASCADE)
    code = models.CharField(max_length=8, default=generate_random_string, editable=False)
    guest_amount = models.IntegerField()
    total_price = models.FloatField()
    comment= models.TextField(max_length=1000)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.check_out < self.check_in:
            raise ValidationError({
                "check_out": _("Check out date must not be before check in")
            }, code="invalid")