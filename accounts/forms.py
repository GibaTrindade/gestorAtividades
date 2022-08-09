from django.forms import ModelForm
from .models import User
from django.contrib import messages


class FormUpdateUser(ModelForm):
    class Meta:
        model = User
        fields = ('matricula', 'chefia', 'setor', 'entrada',
                  'saidaAlmoco', 'voltaAlmoco', 'saida')
