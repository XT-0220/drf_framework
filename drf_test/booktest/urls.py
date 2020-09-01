# from django.urls import re_path
# from booktest import views
#
# urlpatterns = [
#     re_path(r'^books/$', views.BooKInfoViewSet.as_view({
#         "get":'list',
#         "post":'create',
#     })),
#     re_path(r'^books/(?P<pk>\d+)/$', views.BooKInfoViewSet.as_view({
#         "get": 'retrieve',
#         "put": 'update',
#         "delete": 'destroy',
#     })),
#     re_path(r'^books/latest/$',views.BooKInfoViewSet.as_view({
#         'get':'laster'
#     })),
#     re_path(r'^books/(?P<pk>\d+)/read/$',views.BooKInfoViewSet.as_view({
#         'put':'read'
#     }))
# ]


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


from booktest import views
urlpatterns = [
]
# 1.创建Router对象。
from rest_framework.routers import SimpleRouter
router = SimpleRouter()

# 2.注册视图集
router.register('books', views.BooKInfoViewSet, basename='books')

# 3.添加路由数据
urlpatterns += router.urls