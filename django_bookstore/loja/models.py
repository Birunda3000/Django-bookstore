from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

def validate_interval(value):
    if value < 0:
        raise ValidationError('Preço não pode ser menor que zero')

def validate_interval_age(value):
    if value < 16:
        raise ValidationError('Apenas para maiores de 16 anos')

def validate_interval_quantidade(value):
    if value < 0:
        raise ValidationError('quantidade negativa')

# Create your models here.

class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True, validators=[validate_interval_age])#maxdigits e a idade não é obrigatoria

class Genero(models.Model):
    nome = models.CharField(max_length=50)
    data_criação = models.DateTimeField(auto_now_add=True)
    descrição = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Generos'
    #resolvendo o object no admim nome melhor
    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    data_criação = models.DateTimeField(auto_now_add=True)
    endereço = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = 'Editoras'
    #resolvendo o object no admim nome melhor
    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    sinopse = models.TextField(null=True, blank=True)
    data_criação = models.DateTimeField(auto_now_add=True)

    preço = models.DecimalField(decimal_places=2, max_digits=9,validators=[validate_interval])
    image = models.FileField(upload_to='products/', null=True, blank=True)
    image2 = models.FileField(upload_to='products/', null=True, blank=True)
    image3 = models.FileField(upload_to='products/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Livros'
    #resolvendo o object no admim nome melhor
    def __str__(self):
        return self.titulo



'''class CartManager(models.manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id = cart_id)
        if qs.count == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticate and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user = request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user = None):
        user_obj = None
        if user is not None:
            if user.is_authenticate:
                user_obj = user
        return self.model.objects.create(user = user_obj)'''





#User = settings.AUTH_USER_MODEL
class Cart(models.Model):    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    products = models.ManyToManyField(Livro, blank = True)
    total = models.DecimalField(default = 0.00, max_digits=100, decimal_places = 2)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    #objects = CartManager()

    def __str__(self):
        return str(self.id)
