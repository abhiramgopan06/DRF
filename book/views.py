from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import book
from .serializers import bookserializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookViewSet(ModelViewSet):
    queryset = book.objects.all()
    serializer_class = bookserializers

class BookAPIView(APIView):
    def get(self , response):
        books = book.objects.all()
        serializers = bookserializers(books,many=True)
        print(serializers)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = bookserializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status.HTTP_201_CREATED)
        return Response(serializers.error,status.HTTP_400_BAD_REQUEST)