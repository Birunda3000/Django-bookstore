from django.shortcuts import render, redirect
import datetime
from .models import Genero, Editora, Livro, Compra, Forma_de_Pagamento#, Cart
from django.contrib.auth.decorators import login_required

#from django.contrib.auth.forms import UserCreationForm

from decimal import *

from .forms import UserCreationForm, UserChangeForm, CompraForm, AvaliacaoForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def home(request):
    book_list = Livro.objects.all().order_by('genero')
    paginator = Paginator(book_list, 6)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'loja/home.html', {'books':books})

def book_page(request, pk):
    data = {}
    livro = Livro.objects.get(pk=pk)
    data['livro'] = livro
    return render(request,'loja/book_page.html',data)

def search_view(request):
    dados = request.GET["dados"]
    method = request.GET["method"]
    data = {}
    if method == "Titulo":
        livro = Livro.objects.filter(titulo=dados)
    elif method == "Autor":
        livro = Livro.objects.filter(autor=dados)
    elif method == "Genero":
        p = Genero.objects.get(nome=dados)
        livro = Livro.objects.filter(genero=p.pk)
    elif method == "Editora":
        p = Editora.objects.get(nome=dados)
        livro = Livro.objects.filter(editora=p.pk)
    data['livros'] = livro
    return render(request, 'loja/search_view.html', data)

@login_required
def compra(request, pk):
    compra = Compra()
    compra.livro = Livro.objects.get(pk=pk)
    k = Livro.objects.get(pk=pk)
    compra.user = request.user
    compra.valor = k.preço

    '''   nome = Forma_de_Pagamento.objects.get(pk=form['metodo_de_pagamento'])


    qualquer = form['metodo_de_pagamento'].value

    print(qualquer)

    if qualquer == 1 or qualquer == 'Boleto' or qualquer == '1' or qualquer == int(1) or nome.nome == 'Boleto':
        compra.valor = float(k.preço)*0.9

    else:
        compra.valor = float(k.preço)*0.9''' 
    
    form = CompraForm(request.POST or None, instance = compra)
    data = {}
    data['form'] = form 
    data['livro'] = Livro.objects.get(pk=pk)
    
    if form.is_valid():
        form.save()
        return redirect('url_user_page')
    return render(request,'loja/compra.html', data)

    




@login_required
def user_page(request):
    data = {}
    data['livros'] = Livro.objects.all()# forma errada
    data['compras'] = Compra.objects.filter(user=request.user).order_by('timestamp').reverse()
    return render(request,'loja/user_page.html', data)

@login_required
def edit_user(request):
    form = UserChangeForm(request.POST or None, instance = request.user)
    data = {}
    data['form'] = form 
    """ data['livros'] = Livro.objects.all()# forma errada
    data['compras'] = Compra.objects.filter(user=request.user).order_by('timestamp').reverse() """
    if form.is_valid():
        form.save()
        return redirect('url_user_page')
    return render(request,'loja/edit_user.html', data)

@login_required
def cart_home(request):
    return render(request, "loja/carts.html", {} )

@login_required
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('url_user_page')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'loja/alterar_senha.html', {'form_senha': form_senha})


@login_required
def relatorio(request):
    date = request.GET["date"]
    data = {}
    
    data['Compras'] = Compra.objects.filter(timestamp2 = date)#'2021-02-23')
    data['Livros'] = Livro.objects.all()



    p = Compra.objects.filter(timestamp2 = date)
    x = 0
    for compra in p:
        x = x + compra.valor
    data['soma'] = x
    return render(request,'loja/relatorio.html', data)


@login_required
def avaliar(request, pk):
    nota1 = request.GET["nota"]
    pkCompra = request.GET["pkCompra"]
    
    nota = float(nota1)
    
    livro = Livro.objects.get(pk=pk)

    compra = Compra.objects.get(pk=pkCompra)
    compra.avaliado = True
    compra.save()
    #form = AvaliacaoForm(request.POST or None, instance = livro)
    
    nota_atual = livro.nota
    avaliacoes_atuais = livro.numero_de_avaliacoes
    pontos = nota_atual*avaliacoes_atuais
    
    pontos_novos = pontos + nota
    
    avaliacoes_atuais = avaliacoes_atuais + float(1)
    
    nota_atual = pontos_novos / avaliacoes_atuais
    
    livro.nota = nota_atual
    livro.numero_de_avaliacoes = avaliacoes_atuais
    livro.save()

    
    #form.nota = nota_atual
    #form.numero_de_avaliacoes = avaliacoes_atuais
    #form.save()
    return redirect('url_user_page')






@login_required
def cart_home(request):
    data = {}
    carrinho = Cart.objects.filter(user=request.user)
 
    '''products = carrinho.products.all()
    total = 0
    for product in products:
        total += product.price
    print(total)
    carrinho.total = total
    carrinho.save()'''

    data['carrinho'] = carrinho
    return render(request,'loja/carts.html', data)

'''def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {})'''