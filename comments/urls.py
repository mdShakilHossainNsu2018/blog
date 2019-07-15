from django.urls import path
from .views import (comment_thread, comment_delete)


app_name = 'comments'

urlpatterns = [
    path('<int:id>/', comment_thread, name='thread'),
    # path('create/', post_create, name='create_posts'),
    # path('<slug:slug>/', post_detail, name='detail'),
    #
    # path('<slug:slug>/edit/', post_update, name='update'),
    path('<int:id>/delete/', comment_delete, name='delete'),

]
