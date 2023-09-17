from django.db import models

class Realties(models.Model):
    id = models.AutoField(primary_key=True)
    guest_limit = models.IntegerField()
    bath_amount = models.IntegerField()
    pets_allowed = models.BooleanField(default=False)
    cleaning_fee = models.FloatField()
    activated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"id={self.id}, created_at{self.created_at}, updated_at={self.updated_at}"
