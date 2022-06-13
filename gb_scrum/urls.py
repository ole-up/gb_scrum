from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import mainapp.views as mainapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path("design/", mainapp.habr, name="design"),
    path("web/", mainapp.habr, name="web"),
    path("mobile/", mainapp.habr, name="mobile"),
    path("marketing/", mainapp.habr, name="marketing"),
    path("help/", mainapp.help, name="help"),
    path("personal/", include("personalapp.urls", namespace='personal')),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
