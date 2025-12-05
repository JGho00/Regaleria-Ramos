from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_productos, name='listado_productos'),
    path('<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]