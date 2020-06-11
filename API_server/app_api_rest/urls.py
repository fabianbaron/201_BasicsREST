from django.urls import path, include

from rest_framework import routers  # Crea Urls para todos los objetos de la vista

from .views import ListaEmpleadosView, EmpleadosView

myrouter = routers.DefaultRouter()
myrouter.register('empleados_api', EmpleadosView, basename=None)

urlpatterns = [
    path('empleados/', ListaEmpleadosView.as_view(), name='Lista de empleados JSON'),
    path('', include(myrouter.urls))
]
