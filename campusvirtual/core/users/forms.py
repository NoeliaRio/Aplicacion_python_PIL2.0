from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import Group

from core.users.models import User


class UserForm(ModelForm):
    username = forms.CharField(
        label='Nombre de usuario *',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese un nombre de usuario identificador',
                'autofocus': True,
                'class': 'form-control'
            }
        )
    )
    email = forms.CharField(
        label='Correo electrónico *',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese una dirección de correo electrónico',
                'class': 'form-control'
            }
        )
    )
    first_name = forms.CharField(
        label='Nombres del usuario *',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el/los nombre/s del usuario',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label='Apellidos del usuario *',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el/los apellido/s del usuario',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña *',
        widget=forms.PasswordInput(
            render_value=True,
            attrs={
                'placeholder': 'Ingrese una contraseña',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        exclude = ['id', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at', 'last_login', 'groups']
    
    def save(self, commit=True): 
        form = super()
        data = {}

        if form.is_valid():
            pwd = self.cleaned_data['password']
            u = form.save(commit=False)
            if u.pk is None:
                u.set_password(pwd)
                data = u
            else:
                user = User.objects.get(pk=u.pk)
                if user.password != pwd:
                    u.set_password(pwd)
            u.save()

            # asignar grupo "usuario"
            technician_group, created = Group.objects.get_or_create(name='Usuario') 
            technician_group.user_set.add(u)

            return u
        else:
            data['error'] = form.errors
        return data


class UpdateUserForm(ModelForm):
    username = forms.CharField(
        label='Nombre de usuario *',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese un nombre de usuario identificador',
                'autofocus': True,
                'class': 'form-control'
            }
        )
    )
    email = forms.CharField(
        label='Correo electrónico *',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese una dirección de correo electrónico',
                'class': 'form-control'
            }
        )
    )
    first_name = forms.CharField(
        label='Nombres del usuario *',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el/los nombre/s del usuario',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label='Apellidos del usuario *',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el/los apellido/s del usuario',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        exclude = ['id', 'password', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at', 'last_login', 'groups']
