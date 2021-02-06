from django.shortcuts import render
import datetime
from .models import Genero, Editora, Livro
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