from django.contrib import admin
from .models import Tabela, Atividade, ItemTabela


class ItemInline(admin.TabularInline):
    model = ItemTabela
    extra = 1


class TabelaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'mes', 'autor',)
    inlines = [
        ItemInline,
    ]


class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'duracao', 'autor',)



class ItemTabelaAdmin(admin.ModelAdmin):

    list_display = ('data', 'tabela',)


admin.site.register(Tabela, TabelaAdmin)
admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(ItemTabela, ItemTabelaAdmin)
