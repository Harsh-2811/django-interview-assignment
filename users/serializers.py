from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','role','contact_number','is_superuser','password']


    def to_representation(self, instance):
        response = super().to_representation(instance)
        del response['password']
        return response


