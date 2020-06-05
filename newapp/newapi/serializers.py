from rest_framework import serializers
from .models import AppUser, SigninResponse

class AppUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppUser
        fields = ('username', 'password', 'created_at')
    

class SigninResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SigninResponse
        if model.status:
            fields = ('status', 'message')
        else:
            fields = ('status', 'message', 'token', 'response_created', 'username')
            
