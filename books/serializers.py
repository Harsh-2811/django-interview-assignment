
from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','author','status']
        read_only_fields = ['added_by']
    

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"
        