from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import Index, TabelaAdd, TabelaDelete, \
    TabelaUpdate, ItemAdd, ItemDelete, ItemUpdate,\
    AtividadeAdd, AtividadeDelete, AtividadeUpdate,\
    TabelaDetalhe, AtividadeDetalhe


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tabela/<int:pk>', TabelaDetalhe.as_view(), name='tabela_detalhes'),
    path('tabela/delete/<int:pk>/', csrf_exempt(TabelaDelete.as_view()), name='tabela_delete'),
    path('tabelaAdd/', TabelaAdd.as_view(), name='tabela_add'),
    path('atividade/<int:pk>', AtividadeDetalhe.as_view(), name='atividade_detalhe'),
    path('atividadeAdd/', AtividadeAdd.as_view(), name='atividade_add'),
    path('item/delete/<int:pk>/', csrf_exempt(ItemDelete.as_view()), name='item_delete'),
]