from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def render_posts(request):
    posts= Post.objects.all()
    
    return render(request, 'posts.html', {"posts": posts})

def post_detalle(request, post_id):
    post = get_object_or_404(Post, pk=post_id) #Pk primary key, detecta si hay una pagina con este id, si no 404
    return render(request,'post_detalle.html', {'post': post})