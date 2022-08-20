from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework import generics, mixins
# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

User  = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    parser_classes = [FormParser]
    serializer_class = MyTokenObtainPairSerializer

class Registration(generics.GenericAPIView):   
    serializer_class = UserSerializer
    parser_classes = [FormParser]
    
    def post(self, request, *args, **kwargs):
        data = request.data
        if 'username' not in data or 'role' not in data or 'password' not in data or 'contact_number' not in data :
            return Response("Please Enter Proper and Complete data",status=status.HTTP_204_NO_CONTENT)
        
        if not User.objects.filter(username = data['username']).exists():
            user = User.objects.create_user(
                username = data['username'],
                email = data['username'],
                role = str(data['role']).upper(),
                password = data['password'],
                contact_number = data['contact_number'],
            )
            return Response(UserSerializer(user,many=False).data,status=status.HTTP_201_CREATED)
        else:
            return Response("User already exists",status=status.HTTP_409_CONFLICT)

class CheckIfLIBRARIAN(IsAuthenticated):

    def has_permission(self, request, view):
        resp = super(CheckIfLIBRARIAN, self).has_permission(request, view)
        return getattr(request.user, "role", None) == "LIBRARIAN" and resp


class createMember(generics.CreateAPIView):
    parser_classes = [FormParser]
    permission_classes = [CheckIfLIBRARIAN]
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        obj = serializer.save()
        print(obj.id)

class listOutMember(generics.ListAPIView):
    queryset = User.objects.filter(role="MEMBER").order_by('-created_at')
    permission_classes = [CheckIfLIBRARIAN]
    serializer_class = UserSerializer


class updateMember(generics.UpdateAPIView):
    parser_classes = [FormParser]
    queryset = User.objects.filter(role="MEMBER").order_by('-created_at')
    permission_classes = [CheckIfLIBRARIAN]
    serializer_class = UserSerializer
    lookup_url_kwarg  = 'id'

class retriveMember(generics.RetrieveAPIView):
    queryset = User.objects.filter(role="MEMBER").order_by('-created_at')
    permission_classes = [CheckIfLIBRARIAN]
    serializer_class = UserSerializer
    lookup_url_kwarg  = 'id'

class deleteMember(generics.DestroyAPIView):
    queryset = User.objects.filter(role="MEMBER").order_by('-created_at')
    permission_classes = [CheckIfLIBRARIAN]
    serializer_class = UserSerializer
    lookup_url_kwarg  = 'id'


class deleteMyAccount(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user=self.request.user
        user.delete()

        return Response("Your account is Deleted",status=status.HTTP_200_OK)