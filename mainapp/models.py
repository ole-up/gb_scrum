from django.db import models
from sequences import Sequence

from authapp.models import CustomUser

comment_ids = Sequence("mainapp_comment")


class ArticleCategory(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=64, unique=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Заголовок", max_length=150)
    image = models.ImageField(upload_to="article_images", blank=True)
    description = models.TextField(verbose_name="Содержание", blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    for_moderation = models.BooleanField(default=False)

    class Meta:
        ordering = ['edit_date']

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f"{self.title} ({self.category.name})"


class Comment(models.Model):
    path = models.CharField(verbose_name="Путь", max_length=150)
    level = models.IntegerField(verbose_name="Уровень вложенности")
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    comment_body = models.TextField(verbose_name="Содержимое комментария")
    author = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['path']

