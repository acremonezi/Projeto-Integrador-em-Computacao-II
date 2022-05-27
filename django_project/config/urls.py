"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views as accountsviews


urlpatterns = [
    # Atenção ao caminho do base.html
    # caminho do base: accounts/templates/account/base.html
    # usar {% extends 'account/base.html' %}
    path('', accountsviews.index, name='project_index'), # index page
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # All templates for allauth are in django_project/accounts/templates/account the base.html for the project
    path('accounts/', include('allauth.urls')),
]
