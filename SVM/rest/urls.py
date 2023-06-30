from django.urls import path, include
from rest_framework import routers
from . import views
from .views import HabitacionViewSet

router = routers.DefaultRouter()
router.register('reporte',views.HabitacionViewSet)

urlpatterns = [
    path('',include(router.urls))
]