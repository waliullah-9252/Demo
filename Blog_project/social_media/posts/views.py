from django.shortcuts import render,redirect
from .import forms
from .import models

# Create your views here.

def add_post(request):
    if request.method == 'POST':
        post_forms = forms.PostForm(request.POST)
        if post_forms.is_valid():
            post_forms.save()
            return redirect('add_post')
    else:
        post_forms = forms.PostForm()
    return render(request, 'posts/add_post.html', {'form': post_forms})


def edit_post(request,id):
    post = models.Posts.objects.get(pk = id)
    post_forms = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_forms = forms.PostForm(request.POST, instance=post)
        if post_forms.is_valid():
            post_forms.save()
            return redirect('homepage')

    return render(request, 'posts/add_post.html', {'form': post_forms})

def delete_post(request,id):
    delete = models.Posts.objects.get(pk = id).delete()
    return redirect('homepage')

def complete_post(request):
    complete_posts = models.Posts.objects.get(pk=id)
    complete_posts.is_complete = True
    complete_posts.save()
    return redirect('homepage')
