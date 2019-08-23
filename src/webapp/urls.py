from django.urls import include, path

from . import views

from django.contrib.auth.decorators import login_required
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('social_django.urls')),
    path('logout/', views.logout),
]

admin.autodiscover()
admin.site.login = login_required(admin.site.login)