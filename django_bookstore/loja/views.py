from django.shortcuts import render
import datetime
from .models import Genero, Editora, Livro

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    data = {}
    data['livros'] = Livro.objects.all()

    #html = "<html><body>    meu primiero site dijango It is now %s.</body></html>" % now
    #return HttpResponse(html)
    return render(request, 'loja/home.html', data)

def book_page(request, pk):
    data = {}
    livro = Livro.objects.get(pk=pk)
    data['livro'] = livro
    return render(request,'loja/book_page.html',data)

@login_required
def compra(request, pk):
    data = {}
    livro = Livro.objects.get(pk=pk)
    data['livro'] = livro
    return render(request,'loja/compra.html',data)