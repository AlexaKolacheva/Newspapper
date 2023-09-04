from django.db import models
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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']

    # def get_absolute_url(self):
    #    return reverse("article_detail", kwargs={"pk": self.pk})


class Comments(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField( default='Type some text here...')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
