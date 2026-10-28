from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # Пункт A: Author
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # Пункт B: Draft/Published
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    # Пункт D: Categories & Tags (Простой вариант)
    category = models.CharField(max_length=100, default='General')
    tags = models.CharField(max_length=200, blank=True, help_text="Write tags separated by commas (e.g. IT, Python)")

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

# Пункт C: Comments Moderation
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Вот это поле active - для модерации (True = опубликовано, False = скрыто)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'