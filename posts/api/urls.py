from django.urls import path
from .views import (PostListAPIView)


app_name = 'posts-api'

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    # path('create/', post_create, name='create_posts'),
    # path('<slug:slug>/', post_detail, name='detail'),
    #
    # path('<slug:slug>/edit/', post_update, name='update'),
    # path('<slug:slug>/delete/', post_delete, name='delete'),

]
