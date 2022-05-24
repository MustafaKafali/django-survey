from . import models
from rest_framework import viewsets, permissions
from . import serializers


class CevaplarViewSet(viewsets.ModelViewSet):
    queryset = models.Cevaplar.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = serializers.CevaplarSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = serializers.UserSerializer