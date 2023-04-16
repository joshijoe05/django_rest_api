from django.shortcuts import render
from rest_framework import generics
from .serializers import BlogsSerializer
from .models import Blogs

# Create your views here.
class BlogList(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

class BlogCreate(generics.CreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

class BlogRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer