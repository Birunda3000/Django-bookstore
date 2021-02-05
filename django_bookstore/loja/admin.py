from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import Genero, Editora, Livro, User

from .forms import UserChangeForm, UserCreationForm

# Register your models here.
admin.site.register(Genero)
admin.site.register(Editora)
admin.site.register(Livro)
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Personal Info", {"fields": ("age",)}),
    )
