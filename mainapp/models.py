from django.db import models
from django.utils.timezone import datetime


class HabrCategory(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=64, unique=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    category_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Habr(models.Model):
    category = models.ForeignKey(HabrCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Заголовок", max_length=70)
    image = models.ImageField(upload_to="article_images", blank=True)
    short_desc = models.CharField(verbose_name="Аннотация", max_length=256, blank=True)
    description = models.TextField(verbose_name="Содержание", blank=True)
    article_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        ordering = ['-article_date']
