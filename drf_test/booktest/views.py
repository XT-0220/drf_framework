from django.http import Http404
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet
from rest_framework.response import Response
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer
from rest_framework.authentication import SessionAuthentication

class BooKInfoViewSet(ModelViewSet):

    lookup_value_regex = '\d+'
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

    # 指定当前视图自己的认证方案，不再使用全局认证方案
    authentication_classes = [SessionAuthentication]

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