from django.db import router
from rest_framework import routers
from . import viewset

router = routers.DefaultRouter()
router.register('cevap', viewset.CevaplarViewSet, 'cevap')
router.register('user', viewset.UserViewSet, 'user')


urlpatterns = router.urls