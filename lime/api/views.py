from rest_framework import generics
from ..models import Category,Bookmark,Search
from .serializers import CategorySerializer,BookmarkSerializer,SearchSerializer
from rest_framework import viewsets

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer