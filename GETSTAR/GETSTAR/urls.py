from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('comunicados/', views.comunicados, name="comunicados"),
    path('buscar/', views.buscar, name="buscar"),
]
