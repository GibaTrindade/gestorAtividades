from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .views import Index, TabelaAdd, TabelaDelete, \
    TabelaUpdate, ItemAdd, ItemDelete, ItemUpdate,\
    AtividadeAdd, AtividadeDelete, AtividadeUpdate,\
    TabelaDetalhe, AtividadeDetalhe


urlpatterns = [
    path('', login_required(Index.as_view(), redirect_field_name='login'), name='index'),
    path('tabela/<int:pk>', login_required(TabelaDetalhe.as_view(), redirect_field_name='login'), name='tabela_detalhes'),
    path('tabela/delete/<int:pk>/', csrf_exempt(TabelaDelete.as_view()), name='tabela_delete'),
    path('tabelaAdd/', login_required(TabelaAdd.as_view(), redirect_field_name='login'), name='tabela_add'),
    path('atividade/<int:pk>', login_required(AtividadeDetalhe.as_view(), redirect_field_name='login'), name='atividade_detalhe'),
    path('atividadeAdd/', login_required(AtividadeAdd.as_view(), redirect_field_name='login'), name='atividade_add'),
    path('item/delete/<int:pk>/', csrf_exempt(ItemDelete.as_view()), name='item_delete'),
]