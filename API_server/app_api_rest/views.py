from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Empleados
from .serializador import EmpleadosSerializer


# Create your views here.

class ListaEmpleadosView(APIView):

    def get(self, request):
        empleados1 = Empleados.objects.all()  # Query a la base de datos de la app
        serializador = EmpleadosSerializer(empleados1, many=True)
        return Response(serializador.data)

    def post(self, request, json_):
        pass


#  Otra forma de hacerlo
class EmpleadosView(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
