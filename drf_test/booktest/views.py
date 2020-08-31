# from rest_framework import status
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import mixins
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ModelViewSet
# from booktest.serializers import BookInfoSerializer
# from booktest.models import BookInfo
# import json
# from django.http import JsonResponse, HttpResponse, Http404
# from django.views import View





import json
from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin

class BookInfoViewSet(ModelViewSet):
    """视图集"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

# /books/
class BookListView(GenericAPIView,
                   ListModelMixin,
                   CreateModelMixin):
    # 指定序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()

    def get(self, request):
        """
        获取所有图书数据:
        ① 查询数据库获取所有图书数据
        ② 将所有图书数据通过json进行返回
        """

        # books = self.get_queryset()
        #
        # serializer = self.get_serializer(books,many=True)
        #
        # serializer.save()
        #
        # return Response(serializer.data)
        return self.list(request)


    def post(self, request):
        """
        新增一本图书数据:
        ① 获取参数并进行校验
        ② 创建图书数据并保存到数据库
        ③ 将新增图书数据通过json进行返回
        """

        # serializer = self.get_serializer(data=request.data)
        #
        # serializer.is_valid(raise_exception=True)
        #
        # serializer.save()
        #
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.create(request)

# /books/(?P<pk>\d+)/
class BookDetailView(GenericAPIView,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin):

    # 指定序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()

    def get(self, request, pk):
        """
        获取指定图书数据(根据pk):
        ① 查询数据库获取指定的图书数据
        ② 将指定图书数据通过json进行返回
        """

        # book = self.get_object()
        #
        # serializer = BookInfoSerializer(book)
        #
        # serializer.save()
        #
        # return Response(serializer.data)
        return self.retrieve(request)

    def put(self, request, pk):
        """
        修改指定图书数据(根据pk):
        ① 查询数据库获取指定的图书数据
        ② 获取参数并进行校验
        ③ 修改图书数据并保存到数据库
        ④ 将修改图书数据通过json进行返回
        """

        # book = self.get_object()
        #
        # serializer = BookInfoSerializer(book,data=request.data)
        #
        # serializer.is_valid(raise_exception=True)
        #
        # serializer.save()
        #
        # return Response(serializer.data)
        return self.update(request)

    def delete(self, request, pk):
        """
        删除指定图书数据(根据pk):
        ① 查询数据库获取指定的图书数据
        ② 删除指定图书数据
        ③ 返回响应
        """

        # book = self.get_object()
        #
        # book.delete()
        #
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return self.destroy(request)