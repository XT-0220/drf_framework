from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from booktest.serializers import BookInfoSerializer
from booktest.models import BookInfo
import json
from django.http import JsonResponse, HttpResponse, Http404
from django.views import View


class BookInfoViewSet(ModelViewSet):
    """视图集"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

# /books/
class BookListView(ListCreateAPIView):

    serializer_class = BookInfoSerializer

    queryset = BookInfo.objects.all()



class BookDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class= BookInfoSerializer

    queryset = BookInfo.objects.all()
