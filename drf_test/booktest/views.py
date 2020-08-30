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


# class BookInfoViewSet(ModelViewSet):
#     """视图集"""
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#
# # /books/
# class BookListView(ModelViewSet):
#
#     serializer_class = BookInfoSerializer
#
#     queryset = BookInfo.objects.all()
#
#
#
# class BookDetailView(ModelViewSet):
#
#     serializer_class= BookInfoSerializer
#
#     queryset = BookInfo.objects.all()



import json
from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer
from rest_framework.response import Response
from rest_framework import status
class BookInfoViewSet(ModelViewSet):
    """视图集"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

# /books/
class BookListView(APIView):
    def get(self, request):
        """
        获取所有图书数据:
        ① 查询数据库获取所有图书数据
        ② 将所有图书数据通过json进行返回
        """
        # ① 查询数据库获取所有图书数据
        books = BookInfo.objects.all()

        # ② 将所有图书数据通过json进行返回
        # books_li = []
        #
        # for book in books:
        #     book_dict = {
        #         'id': book.id,
        #         'btitle': book.btitle,
        #         'bpub_date': book.bpub_date,
        #         'bread': book.bread,
        #         'bcomment': book.bcomment
        #     }
        #     books_li.append(book_dict)
        serializer = BookInfoSerializer(books,many=True)
        serializer.save()

        return Response(serializer.data)

    def post(self, request):
        """
        新增一本图书数据:
        ① 获取参数并进行校验
        ② 创建图书数据并保存到数据库
        ③ 将新增图书数据通过json进行返回
        """
        # ① 获取参数并进行校验
        # req_dict = json.loads(request.body.decode())   === request.data

        serializer = BookInfoSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        # btitle = req_dict.get('btitle')
        # bpub_date = req_dict.get('bpub_date')
        #
        # # TODO: 省略参数校验过程...
        #
        # # ② 创建图书数据并保存到数据库
        # book = BookInfo.objects.create(btitle=btitle,
        #                                bpub_date=bpub_date)
        #
        # # ③ 将新增图书数据通过json进行返回
        # book_dict = {
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bpub_date': book.bpub_date,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment
        # }

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# /books/(?P<pk>\d+)/
class BookDetailView(View):
    def get(self, request, pk):
        """
        获取指定图书数据(根据pk):
        ① 查询数据库获取指定的图书数据
        ② 将指定图书数据通过json进行返回
        """
        # ① 查询数据库获取指定的图书数据
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            # 图书不存在
            # return JsonResponse({'detail': 'not found'}, status=404)
            raise Http404
        # ② 将指定图书数据通过json进行返回
        # book_dict = {
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bpub_date': book.bpub_date,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment
        # }
        serializer = BookInfoSerializer(book)
        serializer.save()

        return Response(serializer.data)

    def put(self, request, pk):
        """
        修改指定图书数据(根据pk):
        ① 查询数据库获取指定的图书数据
        ② 获取参数并进行校验
        ③ 修改图书数据并保存到数据库
        ④ 将修改图书数据通过json进行返回
        """
        # ① 查询数据库获取指定的图书数据
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            # 图书不存在
            raise Http404
        # ② 获取参数并进行校验
        req_dict = json.loads(request.body.decode())

        serializer = BookInfoSerializer(book,data=req_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # btitle = req_dict.get('btitle')
        # bpub_date = req_dict.get('bpub_date')
        #
        # # TODO: 省略参数校验过程...
        #
        # # ③ 修改图书数据并保存到数据库
        # book.btitle = btitle
        # book.bpub_date = bpub_date
        # book.save()
        #
        # # ④ 将修改图书数据通过json进行返回
        # book_dict = {
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bpub_date': book.bpub_date,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment
        # }

        return Response(serializer.data)

    def delete(self, request, pk):
        """
        删除指定图书数据(根据pk):
        ① 查询数据库获取指定的图书数据
        ② 删除指定图书数据
        ③ 返回响应
        """
        # ① 查询数据库获取指定的图书数据
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            # 图书不存在
            raise Http404
        # ② 删除指定图书数据
        book.delete()

        # ③ 返回响应
        return Response(status=status.HTTP_204_NO_CONTENT)