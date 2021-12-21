from books.models import Book, HeroInfo
from books.serializer import BookSerializer, HeroInfoSerializer
from rest_framework import serializers, viewsets

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class HeroInfoViewset(viewsets.ModelViewSet):
    queryset = HeroInfo.objects.all()
    serializer_class = HeroInfoSerializer












    
