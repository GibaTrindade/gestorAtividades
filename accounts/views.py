from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def cadastro(request):
    return render(request, 'cadastro.html')


