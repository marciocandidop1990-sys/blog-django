from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


def home(request):
    meus_posts = Post.objects.all().order_by('-data_publicacao')

    paginator = Paginator(meus_posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }

    return render(request, "home.html", context)


def post_detalhe(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post_detalhe.html", {"post": post})