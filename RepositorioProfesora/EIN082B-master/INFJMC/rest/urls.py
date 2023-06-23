from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CarreraViewSet

router = routers.DefaultRouter()
router.register('carrera',views.CarreraViewSet)

urlpatterns = [
    path('',include(router.urls))
]