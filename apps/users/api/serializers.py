from rest_framework import serializers
from apps.users.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'id', 
            'username', 
            'name', 
            'email', 
            'image', 
            'is_staff', 
            'role', 
            'address', 
            'location', 
            'province', 
            'phone'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.image = validated_data.get('image', instance.image)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.role = validated_data.get('role', instance.role)
        instance.address = validated_data.get('address', instance.address)
        instance.location = validated_data.get('location', instance.location)
        instance.province = validated_data.get('province', instance.province)
        instance.phone = validated_data.get('phone', instance.phone)

        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance
