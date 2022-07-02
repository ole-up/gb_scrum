from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import mainapp.views as mainapp

urlpatterns = [
    path("", mainapp.articles, name="index"),
    path("admin/", admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('articles/', include('mainapp.urls', namespace='articles')),
    path("personal/", include("personalapp.urls", namespace='personal')),
    path('summernote/', include('django_summernote.urls')),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
