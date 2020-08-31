from django.urls import re_path
from booktest import views

urlpatterns = [
    re_path(r'^books/$', views.BoonInfoViewSet.as_view({
        "get":'list',
    })),
    re_path(r'^books/(?P<pk>\d+)/$', views.BoonInfoViewSet.as_view({
        "get":'retrive'
    })),
]


# from django.urls import re_path
# from booktest import views
#
# urlpatterns = [
# ]
#
# # 路由Router
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('books', views.BookInfoViewSet, basename='books')
# urlpatterns += router.urls


