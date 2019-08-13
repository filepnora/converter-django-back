from django.urls import path, include

from . import views
from rest_framework import routers
from .api import PairViewSet

router = routers.DefaultRouter()
router.register('api/pairs', PairViewSet, 'pairs')

urlpatterns = [

    path('', views.converter, name='converter')

]
