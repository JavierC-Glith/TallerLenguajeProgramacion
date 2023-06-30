from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('rest.urls')),

    path('', views.habitaciones_disponibles, name='disponibles'),
    path('ocupadas/', views.habitaciones_ocupadas, name='ocupadas'),
]
