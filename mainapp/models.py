from django.db import models

from authapp.models import CustomUser


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

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f"{self.title} ({self.category.name})"
