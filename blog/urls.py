from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/', include('posts.urls', namespace='posts')),
    path('', TemplateView.as_view(template_name='index.html')),
    # re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name="index.html")),
    # path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += re_path('', TemplateView.as_view(template_name="index.html")),
