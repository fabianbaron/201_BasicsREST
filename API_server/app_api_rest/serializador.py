from rest_framework import serializers  # Permite obtener, crear y actualizar los objetos
from .models import Empleados


class EmpleadosSerializer(serializers.ModelSerializer):  # Serializador: traduce desde y hacia json, xml u otro
    # formato común para transmisión de datos en http
    class Meta:
        model = Empleados
        # fields = ('nombre', 'apellido')  # Opción 1
        fields = '__all__'  # Opción 2 cuando hay pocos campos
