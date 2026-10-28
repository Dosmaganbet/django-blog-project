from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Comment, Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user('author', password='x')
        cls.pub = Post.objects.create(author=user, title='Published', slug='pub', body='Body text',
                                      status='published', category='IT', tags='python')
        cls.draft = Post.objects.create(author=user, title='Secret draft', slug='draft', body='x', status='draft')

    def test_list_shows_only_published(self):
        r = self.client.get(reverse('post_list'))
        self.assertContains(r, 'Published')
        self.assertNotContains(r, 'Secret draft')

    def test_category_filter(self):
        self.assertContains(self.client.get('/?category=IT'), 'Published')
        self.assertNotContains(self.client.get('/?category=Other'), 'Published')

    def test_draft_is_404(self):
        self.assertEqual(self.client.get(reverse('post_detail', args=[self.draft.pk])).status_code, 404)

    def test_add_comment(self):
        url = reverse('post_detail', args=[self.pub.pk])
        r = self.client.post(url, {'name': 'Ann', 'email': 'a@b.co', 'body': 'Nice'})
        self.assertRedirects(r, url)
        self.assertEqual(Comment.objects.filter(post=self.pub).count(), 1)
        self.assertContains(self.client.get(url), 'Nice')

    def test_inactive_comment_hidden(self):
        Comment.objects.create(post=self.pub, name='Bob', email='b@b.co', body='Spam', active=False)
        self.assertNotContains(self.client.get(reverse('post_detail', args=[self.pub.pk])), 'Spam')
