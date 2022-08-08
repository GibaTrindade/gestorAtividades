from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Tabela, Atividade, ItemTabela
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FormItemTabela
from django.urls import reverse, reverse_lazy
from django.contrib import messages
import locale



class Index(ListView):
    model = Tabela
    template_name = 'index.html'
    paginate_by = 6
    context_object_name = 'tabelas'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(autor=self.request.user)

        return qs


class TabelaDetalhe(FormMixin, DetailView):
    template_name = 'tabela_detalhes.html'
    model = Tabela
    form_class = FormItemTabela
    context_object_name = 'tabela'

    def get_success_url(self):
        return reverse('tabela_detalhes', kwargs={'pk': self.object.id})


    def get_context_data(self, **kwargs):
        context = super(TabelaDetalhe, self).get_context_data(**kwargs)
        tabela = self.get_object()
        itensTabela = ItemTabela.objects.filter(tabela=tabela).order_by('data')
        context['itensTabela'] = itensTabela
        context['form'] = FormItemTabela()
        form = context['form']
        form.fields["atividades"].queryset = Atividade.objects.filter(autor=self.request.user).order_by('descricao')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        tabela = self.get_object()
        autor = self.request.user
        data = form.cleaned_data.get('data')
        atividades = form.cleaned_data.get('atividades')
        itemTabela = ItemTabela.objects.create(data=data, tabela=tabela, autor=autor)
        itemTabela.atividades.add(*atividades)
        itemTabela.save()
        messages.success(self.request, 'Item criado com sucesso!')

        return redirect('tabela_detalhes', pk=tabela.id)

    def form_invalid(self, form):
        tabela = self.get_object()
        messages.error(self.request, 'Erro, atividades devem somar 8 horas ou data está inválida!')

        return redirect('tabela_detalhes', pk=tabela.id)


class TabelaAdd(LoginRequiredMixin, CreateView):
    model = Tabela
    fields = ['nome', 'ano', 'mes']
    success_url = '/'
    template_name = 'tabela_form.html'

    def form_valid(self, form):
        nome = form.cleaned_data.get('nome')
        mes = form.cleaned_data.get('mes')
        messages.success(self.request, f'Tabela ({nome} do mês {mes}) criada com sucesso!')

        form.instance.autor = self.request.user
        return super().form_valid(form)



class TabelaUpdate(UpdateView):
    pass


class TabelaDelete(DeleteView):
    model = Tabela

    # success_url = '/'
    def get_success_url(self):
        return reverse_lazy('index')


class ItemAdd(CreateView):
    pass


class ItemUpdate(UpdateView):
    pass


class ItemDelete(DeleteView):
    model = ItemTabela
    #success_url = '/'
    def get_success_url(self):
        return reverse_lazy('tabela_detalhes', kwargs={'pk':self.object.tabela_id})



class AtividadeDetalhe(DetailView):
    pass


class AtividadeAdd(LoginRequiredMixin, CreateView):
    model = Atividade
    fields = ['descricao', 'duracao']
    success_url = '/atividadeAdd/'
    template_name = 'atividade_form.html'

    def form_valid(self, form):
        descricao = form.cleaned_data.get('descricao').upper()
        ducarao = form.cleaned_data.get('duracao')
        messages.success(self.request, f'Atividade ({descricao} - {ducarao}h) criada com sucesso!')
        form.instance.autor = self.request.user
        return super().form_valid(form)

class AtividadeUpdate(UpdateView):
    pass


class AtividadeDelete(DeleteView):
    pass

