from django.contrib import admin

from .models import Habr, HabrCategory

admin.site.register(HabrCategory)
admin.site.register(Habr)
