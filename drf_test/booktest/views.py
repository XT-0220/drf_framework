import json
from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin

class BookInfoViewSet(ModelViewSet):
    """视图集"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


# /books/
class BookListView(ListCreateAPIView):
    # 指定序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()


# /books/(?P<pk>\d+)/
class BookDetailView(RetrieveUpdateDestroyAPIView):

    # 指定序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()