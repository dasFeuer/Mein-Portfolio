from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

#Django admin header customization

admin.site.site_header = " Login to Developer Barun"
admin.site.site_title = "Welcome to Barun's Dashboard"
admin.site.index_title = "Welcome to this Portal"
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)