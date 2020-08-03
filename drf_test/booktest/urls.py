# from django.urls import re_path
# from booktest import views
#
# # urls.py
# urlpatterns = [
#     re_path(r'^books/$', views.BookListView.as_view()),
#     re_path(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view())
# ]


from django.urls import re_path
from booktest import views

urlpatterns = [
]

# 路由Router
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('books', views.BookInfoViewSet, basename='books')
urlpatterns += router.urls


