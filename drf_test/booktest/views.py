from django.http import Http404
from rest_framework import mixins
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet
from rest_framework.response import Response
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class BooKInfoViewSet(ModelViewSet):
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

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