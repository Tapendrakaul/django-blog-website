from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('',views.home_view,name='post_list'),
    path('post/<int:blog_id>/',views.single_post_view,name='post_view'),
    path('search/',views.post_search_view,name="post_search"),
    path('<int:post_id>/share/',views.share_post,name='post_share'),
    
]