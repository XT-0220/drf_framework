from django.http import Http404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class BoonInfoViewSet(ViewSet):

    def list(self,request):
        queryset = BookInfo.objects.all()
        serializer = BookInfoSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrive(self,request,pk):
        try:
            queryset = BookInfo.objects.all()
        except BookInfo.DoesNotExist:
            raise Http404
        serializer = BookInfoSerializer(queryset,many=True)
        return Response(serializer.data)