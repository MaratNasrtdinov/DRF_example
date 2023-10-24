from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers

app_name = 'api'
#
# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#     path('posts/', views.PostList.as_view()),
#     path('posts/<int:pk>/', views.PostDetail.as_view()),
#     path('comments/', views.CommentList.as_view()),
#     path('comments/<int:pk>/', views.CommentDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

router = routers.DefaultRouter()
router.register(r'users', views.UserList)
# router.register(r'users/<int:pk>', views.UserDetail),
router.register(r'posts', views.PostList),
# router.register(r'posts/<int:pk>', views.PostDetail),
router.register(r'comments', views.CommentList),
# router.register(r'comments/<int:pk>', views.CommentDetail)


urlpatterns = [
    path('', include(router.urls)),
]
#

