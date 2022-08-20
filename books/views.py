from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.parsers import FormParser

class CheckIfLIBRARIAN(IsAuthenticated):

    def has_permission(self, request, view):
        resp = super(CheckIfLIBRARIAN, self).has_permission(request, view)
        return getattr(request.user, "role", None) == "LIBRARIAN" and resp

# Create your views here.
class createBook(generics.CreateAPIView):
    parser_classes = [FormParser]
    permission_classes = [CheckIfLIBRARIAN]
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        obj = serializer.save()
        print(obj.id)

class listOutBook(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [CheckIfLIBRARIAN]
    def get_queryset(self):
        return  Book.objects.filter(added_by=self.request.user).order_by('-created_at')

class updateBook(generics.UpdateAPIView):
    parser_classes = [FormParser]
    permission_classes = [CheckIfLIBRARIAN]
    serializer_class = BookSerializer
    lookup_url_kwarg  = 'id'

    def get_queryset(self):
        return  Book.objects.filter(added_by=self.request.user).order_by('-created_at')

class retriveBook(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    lookup_url_kwarg  = 'id'
    permission_classes = [CheckIfLIBRARIAN]
    def get_queryset(self):
        return  Book.objects.filter(added_by=self.request.user).order_by('-created_at')

class deleteBook(generics.DestroyAPIView):
    permission_classes = [CheckIfLIBRARIAN]
    serializer_class = BookSerializer
    lookup_url_kwarg  = 'id'

    def get_queryset(self):
        return  Book.objects.filter(added_by=self.request.user).order_by('-created_at')


class borrowBook(APIView):
    parser_classes = [FormParser]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def post(self, request,id, format=None):
        book = self.get_object(id)
        book.status = "BORROWED"
        book.borrowd_by = request.user
        book.save()
        from datetime import datetime
        hisotry = History.objects.create(book = book,borrowd_by = request.user,borrow_date = datetime.today().date())
        return Response("Book {} is Borrowd By {}".format(book.title,request.user.username),status=status.HTTP_201_CREATED)

class returnBook(APIView):
    parser_classes = [FormParser]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def post(self, request,id, format=None):
        book = self.get_object(id)
        book.status = "AVAILABLE"
        book.borrowd_by = None
        book.save()
        from datetime import datetime
        hisotry = History.objects.filter(book = book,borrowd_by = request.user,borrow_date__isnull=False).first()
        if hisotry:
            hisotry.returned_date = datetime.today().date()
            hisotry.save() 
            return Response("Book {} is Released By {}".format(book.title,request.user.username),status=status.HTTP_201_CREATED)
        else:
            return Response("Book {} is Not Borrowd By {}".format(book.title,request.user.username),status=status.HTTP_404_NOT_FOUND)

