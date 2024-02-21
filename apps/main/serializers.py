from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'birth_day', 'age', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'default': True},  
            'age': {'read_only': True}
        }
