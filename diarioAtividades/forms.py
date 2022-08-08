from django.forms import ModelForm
from .models import ItemTabela
from django.contrib import messages

class FormItemTabela(ModelForm):
    def clean(self):
        data = self.cleaned_data
        dataItem = data.get('data')
        atividades = data.get('atividades')
        contador = 0
        for atividade in atividades.all():
            contador += atividade.duracao

        print(contador)

        if contador != 8:
            self.add_error(
                'atividades',
                'Soma das horas precisa ser igual a 8'
            )
        return data


    class Meta:
        model = ItemTabela
        fields = ('data', 'atividades',)