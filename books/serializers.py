
from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"