from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import login, logout, cadastro, UserUpdateView


urlpatterns = [
    path('', login, name='index_login'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('cadastro/', cadastro, name='cadastro'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update'),
]