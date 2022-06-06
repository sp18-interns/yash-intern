from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields= ('title','genre','language','no_of_pages','publisher',)