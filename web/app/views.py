from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def main(request):
    posts = Post.objects.all()
    return render(request, 'app/home.html', {'posts': posts})


def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'app/add.html', {'form': form})


def delete_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        post.delete()
    return redirect('home')


def information(request):
    return render(request, 'app/information.html')


def contacts(request):
    return render(request, 'app/contacts.html')