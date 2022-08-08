from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import login, logout, cadastro


urlpatterns = [
    path('', login, name='index_login'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('cadastro/', cadastro, name='cadastro'),
]