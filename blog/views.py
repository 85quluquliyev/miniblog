from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Blog

def index(request):
    posts = Blog.objects.all().order_by('-id')
    paginator = Paginator(posts, 5)  # Her sayfada 5 nesne
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'posts':posts,
        'page_obj':page_obj
    }
    if request.method == 'POST':
        text_value = request.POST.get('text')
        blog = Blog(text=text_value)
        blog.save()
        return render(request, 'index.html',context)

    return render(request, 'index.html',context)