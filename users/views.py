from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as authLogin
from django.contrib.auth.forms import UserCreationForm

def login(request):

    error = False

    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('login')
            password = request.POST.get('senha')
            user = authenticate(username=username, password=password)

            if user:
                authLogin(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = True
    context = {'form': form, 'error': error }
    return render(request, 'users/login.html', context)

def logout_view(request):
    '''Faz logout do usuário'''
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    '''Faz o cadastro de um novo usuário'''
    if request.method != 'POST':
        # Exibe o formulário de cadastroem branco
        form =  UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do usuário e o redireciona para a página inicial
            authenticated_user = authenticate(username=new_user.username, password = request.POST['password1'])
            authLogin(request, authenticated_user)

            return HttpResponseRedirect(reverse('index'))

    context = { 'form': form }
    return render(request, 'users/register.html', context)