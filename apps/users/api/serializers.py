from rest_framework import serializers
from ..models import Users


from rest_framework import serializers
from ..models import Users

class SerializerClients(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Asegúrate de que la contraseña se reciba en el request

    class Meta:
        model = Users
        fields = ['username', 'email', 'name', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Extrae la contraseña de los datos validados
        user = super().create(validated_data)  # Crea el usuario sin hash
        if password:
            user.set_password(password)  # Hashea la contraseña
            user.save()  # Guarda el usuario con la contraseña hasheada
        return user


from rest_framework import serializers
from ..models import Users

class SerializerEmploye(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Asegúrate de que la contraseña se reciba en el request

    def validate(self, data):
        data['role'] = 'employe'
        return data

    class Meta:
        model = Users
        fields = ['username', 'name', 'email', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Extrae la contraseña de los datos validados
        user = super().create(validated_data)  # Crea el usuario sin hash
        if password:
            user.set_password(password)  # Hashea la contraseña
            user.save()  # Guarda el usuario con la contraseña hasheada
        return user
