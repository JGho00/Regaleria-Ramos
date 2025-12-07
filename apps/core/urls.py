from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_inicio, name='mostrar_inicio'),
    path('/inicio', views.mostrar_inicio, name='inicio'),

]