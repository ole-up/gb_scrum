from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path("habr/", mainapp.habr, name="habr"),
    path("habr/all", mainapp.habr, name="habr_all"),
    path("habr/it", mainapp.habr, name="habr_it"),
    path("habr/yaop", mainapp.habr, name="habr_yaop"),
    path("habr/micro", mainapp.habr, name="habr_micro"),
    path("habr/hackers", mainapp.habr, name="habr_hackers"),
    path("help/", mainapp.help, name="help"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
