from urllib.parse import quote_plus #python 3
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect,Http404
from django.contrib import messages
from django.db.models import Q

from .models import Post
from .forms import PostForm


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None)
    template_name = 'post/post_create.html'
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('list')
    context = {
        "form": form
    }
    return render(request, template_name, context)


def post_detail(request, id=None):
    template_name = 'post/post_detail.html'
    instance = get_object_or_404(Post, id=id)
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "content": instance.content,
        "time": instance.timestamp,
        "instance": instance,
        "share_string": share_string

    }

    return render(request, template_name, context)


def post_list(request):
    template_name = 'post/post_list.html'
    query = Post.objects.all()#.order_by("-timestamp")
    queryset_listuery = request.GET.get("q")
    if query:
        queryset_list = query.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {

        "object": query

    }

    return render(request, template_name, context)


def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    template_name = 'post/post_create.html'
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return redirect('list')

        #return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "content": instance.content,
        "time": instance.timestamp,
        "instance": instance,
        "form": form
    }

    return render(request, template_name, context)


def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, id=id)
    instance.delete()

    return redirect('list')


def all_blog(request):
    template_name = 'post/post_update.html'
    query = Post.objects.all()
    context = {
        "object": query
    }
    return render(request, template_name, context)