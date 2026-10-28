from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import CommentForm
from .models import Post


def published_posts():
    return Post.objects.filter(status='published', publish__lte=timezone.now()).select_related('author')


def post_list(request):
    posts = published_posts()
    category = request.GET.get('category')
    tag = request.GET.get('tag')
    if category:
        posts = posts.filter(category=category)
    if tag:
        posts = posts.filter(tags__icontains=tag)
    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category, 'tag': tag})


def post_detail(request, pk):
    post = get_object_or_404(published_posts(), pk=pk)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})
