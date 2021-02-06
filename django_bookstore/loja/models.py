from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

def validate_interval(value):
    if value < 0:
        raise ValidationError('Preço não poe ser menor que zero')

def validate_interval_age(value):
    if value < 16:
        raise ValidationError('Apenas para maiores de 16 anos')

# Create your models here.

class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True, validators=[validate_interval_age])#maxdigits

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