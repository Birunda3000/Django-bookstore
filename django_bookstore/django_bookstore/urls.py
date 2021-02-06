"""django_bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from loja.views import home, book_page, compra

from django.conf.urls.static import static#***********
from django_bookstore import settings#***********
#import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='url_adm'),#NÃO CONSIGO ACESSAR PELO NOME, VEJA VIEW HOME
    path('home/', home, name='url_home'),
    path("book_page/<int:pk>/", book_page, name='url_book'),
    path("compra/<int:pk>/", compra, name='url_comprar'),

    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)   #depois do +
