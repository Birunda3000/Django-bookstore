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
from loja.views import home, book_page, compra, user_page, cart_home, edit_user, search_view, alterar_senha, relatorio, avaliar

from loja import views

from django.conf.urls.static import static#***********
from django_bookstore import settings#***********
#import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='url_adm'),#NÃO CONSIGO ACESSAR PELO NOME, VEJA VIEW HOME
    path('', home, name='url_home'),
    path("book_page/<int:pk>/", book_page, name='url_book'),
    path("compra/<int:pk>/", compra, name='url_comprar'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts_create/', views.SignUp.as_view(), name= 'signup' ),#ATENÇÃO

    path('user_page/', user_page, name='url_user_page' ),

    path('cart/', cart_home, name='url_cart'),

    path('edit_user/', edit_user, name='url_edit_user'),

    path('search/', search_view, name='url_search_page'),

    path('alterar_senha/', alterar_senha, name='alterar_senha'),

    path('relatorio/', relatorio, name='url_relatorio'),

    path("avaliar/<int:pk>/", avaliar, name='url_avaliar'),

] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)   #depois do +
