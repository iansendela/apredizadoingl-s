from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import forms

# Register your models here.
class CustomUserCreationForm(forms.UserCreationForm):
    """
    Formulário personalizado para criação de usuário.

    Este formulário estende o UserCreationForm padrão do Django e adiciona o campo 'email' à lista de campos.
    Também define a classe 'form-control' para todos os widgets de campo.
    """
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('email',)
        
    def __init__(self, *args, **kwargs): 
        """
        Inicializador do formulário.

        Adiciona a classe 'form-control' a todos os widgets de campo.
        """

        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'

# Registro do modelo User no painel de administração usando o formulário personalizado
admin.site.register(User, CustomUserCreationForm) 