from django.urls import path
from .views import render_posts, post_detalle

app_name = 'blog' #<--- ni idea, por las duda

urlpatterns = [
    path('',render_posts, name='posts'),
    path('<int:post_id>', post_detalle, name='post_detalle'),
]