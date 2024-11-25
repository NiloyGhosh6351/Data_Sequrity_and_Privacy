from django.db import models
from .utils import encrypt_weight, decrypt_weight


class EncryptedIntegerField(models.IntegerField):
    def get_prep_value(self, value):
        # Encrypt the weight before saving to the database
        return encrypt_weight(value)

    # def from_db_value(self, value, expression, connection):
    #     # Decrypt the weight when retrieving from the database
    #     if value is None:
    #         return value
    #     return decrypt_weight(value)


class Patient(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    weight = EncryptedIntegerField()
    height = models.FloatField()
    health_history = models.CharField(max_length=100)
