from django.shortcuts import render
import datetime
from .models import Genero, Editora, Livro, Cart, Compra
from django.contrib.auth.decorators import login_required

#from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreationForm

from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def home(request):
    data = {}
    data['livros'] = Livro.objects.all()
    return render(request, 'loja/home.html', data)

def book_page(request, pk):
    data = {}
    livro = Livro.objects.get(pk=pk)
    data['livro'] = livro
    return render(request,'loja/book_page.html',data)





@login_required
def compra(request, pk):
    compra = Compra()
    compra.livro = Livro.objects.get(pk=pk)
    compra.user = request.user
    compra.save()
    
    data = {}
    data['livro'] = Livro.objects.get(pk=pk)
    return render(request,'loja/compra.html', data)












@login_required
def user_page(request):
    data = {}
    data['livros'] = Livro.objects.all()# forma errada
    data['compras'] = Compra.objects.filter(user=request.user).order_by('timestamp').reverse()
    return render(request,'loja/user_page.html', data)

@login_required
def cart_home(request):
    return render(request, "loja/carts.html", {} )

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