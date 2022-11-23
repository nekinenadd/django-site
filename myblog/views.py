from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request,'myblog/index.html')


def posts(request):
    return render(request,'myblog/posts.html')


def post_detail(request,slug):
    return render(request, 'myblog/post-detail.html')