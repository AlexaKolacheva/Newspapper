from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from accounts.models import CustomUser


class Author(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    @property
    def count_posts(self):
        return self.author_articles.all().count()

    def __str__(self):
        return self.user.get_full_name()




class Category(models.Model):
    category_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Tags(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT,
                               related_name='author_articles')
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image_url = models.ImageField(upload_to='media', blank=True)
    tags = models.ManyToManyField(Tags, blank=True)
    liked = models.ManyToManyField(CustomUser, default=None, blank=True, related_name='Liked')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']

    @property
    def num_likes(self):
        return self.liked.all().count()
    def get_absolute_url(self):
        return reverse("detail_article", kwargs={"pk": self.pk})


class Like(models.Model):

    user = models.ForeignKey(Author, on_delete= models.CASCADE,
                             related_name='user_likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='likes')

    def __str__(self):
        return self.article.title

class Comments(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(default='...')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_date']



