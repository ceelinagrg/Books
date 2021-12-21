from rest_framework import serializers
from books.models import Book, HeroInfo

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name','author','publication','pub_date']

class HeroInfoSerializer(serializers.ModelSerializer):
    hbook = serializers.StringRelatedField()
    class Meta:
        model = HeroInfo
        fields = ['id','hname','hgender', 'hbook']