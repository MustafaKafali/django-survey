from django.db.models import fields
from rest_framework import serializers
from . import models

class CevaplarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cevaplar
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'