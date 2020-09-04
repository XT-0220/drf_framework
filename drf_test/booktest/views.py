from django.http import Http404
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet
from rest_framework.response import Response
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer
from rest_framework.authentication import SessionAuthentication

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        """判断对使用此权限类的视图是否有访问权限"""
        # 任何用户对使用此权限类的视图都有访问权限
        return True

    def has_object_permission(self, request, view, obj):
        """判断对使用此权限类视图中的某个数据对象是否有访问权限"""
        # 需求: 对id为1，3的数据对象有访问权限
        if obj.id in (1, 3):
            return True
        return False

class BooKInfoViewSet(ModelViewSet):

    lookup_value_regex = '\d+'
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

    # 1. 指定当前视图自己的认证方案，不再使用全局认证方案
    authentication_classes = [SessionAuthentication]

    # 2. 使用自定义的权限控制类
    permission_classes = [MyPermission]

    # 3.1分别限流
    # throttle_classes = [AnonRateThrottle]
    # 3.2 此处指定当前视图采用contacts限流频次进行限流
    throttle_scope = 'contacts'

    # def list(self,request):
    #     book = self.get_queryset()
    #     serializer = BookInfoSerializer(book, many=True)
    #     return Response(serializer.data)
    #
    #
    # def retrive(self,request,pk):
    #     try:
    #         book = self.get_object()
    #     except BookInfo.DoesNotExist:
    #         raise Http404
    #     serializer = BookInfoSerializer(book)
    #     return Response(serializer.data)

    # GET /books/latest/ -> lastest
    @action(methods=['get'], detail=False)
    def lastest(self, request):
        return Response({'message': '获取id最新的图书数据'})


    # PUT /books/(?P<pk>\d+)/read/ -> read
    @action(methods=['get'], detail=True)
    def read(self, request, pk):
        return Response({'message': '修改指定图书的阅读量'})