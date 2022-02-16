from django.shortcuts import render

from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated



def auth(request):
    return render(request, 'index.html')





class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['name']
    ordering_fields = ['name', 'price']
    permission_classes = [IsAuthenticated]

