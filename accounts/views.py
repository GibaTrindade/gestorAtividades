from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import User
from .forms import FormUpdateUser
from django.views.generic.edit import UpdateView


# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos!')
        return render(request, 'login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Seja bem vindo!')
        return redirect('index')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    matricula = request.POST.get('matricula')
    chefia = request.POST.get('chefia')
    setor = request.POST.get('setor')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    entrada = request.POST.get('entrada')
    saidaAlmoco = request.POST.get('saidaAlmoco')
    voltaAlmoco = request.POST.get('voltaAlmoco')
    saida = request.POST.get('saida')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not matricula or not chefia or not setor or \
            not email or not usuario or not entrada or not saidaAlmoco or not voltaAlmoco or \
            not saida or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio!')
        return render(request, 'cadastro.html')

    if senha != senha2:
        messages.error(request, 'Os campos de senha e confirmação precisam ser iguais!')
        return render(request, 'cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe!')
        return render(request, 'cadastro.html')

    user = User.objects.create_user(username=usuario, email=email, password=senha,
                                    first_name=nome, last_name=sobrenome,
                                    matricula=matricula, chefia=chefia,
                                    setor=setor, entrada=entrada,
                                    saidaAlmoco=saidaAlmoco, voltaAlmoco=voltaAlmoco,
                                    saida=saida, nome=nome, sobrenome=sobrenome,
                                    usuario=usuario)
    user.save()
    messages.success(request, 'Usuário cadastrado com sucesso!')
    return redirect('login')


class UserUpdateView(UpdateView):
    model = User
    form_class = FormUpdateUser
    template_name = 'update_user.html'
    success_url = '/'
    #fields = ['matricula', 'chefia', 'setor', 'entrada',
    #          'saidaAlmoco', 'voltaAlmoco', 'saida']