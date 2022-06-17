from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import mainapp.views as mainapp

urlpatterns = [
    path("", mainapp.main, name="main"),
    path("admin/", admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth')),
    path("design/", mainapp.habr, name="design"),
    path("help/", mainapp.help, name="help"),
    path("marketing/", mainapp.habr, name="marketing"),
    path("mobile/", mainapp.habr, name="mobile"),
    path("personal/", include("personalapp.urls", namespace='personal')),
    path('summernote/', include('django_summernote.urls')),
    path("web/", mainapp.habr, name="web"),
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
