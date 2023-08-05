
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class PublicacionFormulario(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=30)
    cuerpo = forms.CharField(max_length=999999)
    autor = forms.CharField(max_length=30)
    fecha = forms.DateField()
    imagen = forms.ImageField(required=False)


class LectorFormulario(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)


class ModeradorFormulario(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar eMail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ["email", "password1", "password2", "last_name", "first_name"]
        help_texts = {k:"" for k in fields}


