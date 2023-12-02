from django.shortcuts import render, redirect
from .admin import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout



# Create your views here.
def register(request):
    """ 
    View para registro de usuários.

    Se o método da requisição for POST, tenta validar o formulário de registro.
    Se válido, cria um novo usuário, define 'is_valid' como False e redireciona para a página inicial com uma mensagem de sucesso.
    Caso contrário, exibe uma mensagem de erro no console.

    Se o método da requisição for GET, exibe o formulário de registro.

    :param request: Objeto de requisição HTTP.
    :return: Renderiza a página de registro com o formulário correspondente.
    """
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('home')

        else:
            print('invalid registration details')
            
    return render(request, "registration/register.html",{"form": form})




def user_logout(request):
    """
    View para logout do usuário.

    Realiza o logout do usuário e redireciona para a página inicial.

    :param request: Objeto de requisição HTTP.
    :return: Redireciona para a página inicial.
    """
    logout(request)
    return redirect('home')  