from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.http import HttpResponse
from diarioAtividades.models import Tabela, ItemTabela
import calendar
import datetime

class GerarFrequencia(DetailView):
    model = Tabela
    template_name = 'frequencia.html'
    context_object_name = 'tabela'

    def get_context_data(self, **kwargs):
        context = super(GerarFrequencia, self).get_context_data(**kwargs)
        tabela = self.get_object()
        itensTabela = ItemTabela.objects.filter(tabela=tabela).order_by('data')
        context['itensTabela'] = itensTabela
        listaDiasRemoto=[]
        for item in itensTabela:
            #print(item.data)
            listaDiasRemoto.append(item.data)
        context['listaDiasRemoto'] = listaDiasRemoto
        print(listaDiasRemoto)

        cal = calendar.Calendar()

        def iterMonth(year, month):
            for day in cal.itermonthdays(year, month):
                if day > 0:
                    yield datetime.date(year, month, day)

        listaDiasMes = []
        diasSemana = []
        ano = tabela.ano
        mes = tabela.mes
        for d in iterMonth(ano, mes):
            #d = d.strftime("%d/%m/%Y")

            listaDiasMes.append(d)
            diaSemana = d.strftime("%A")
            if diaSemana == 'Monday':
                diasSemana.append("Segunda")
            elif diaSemana == 'Tuesday':
                diasSemana.append("Terça")
            elif diaSemana == 'Wednesday':
                diasSemana.append("Quarta")
            elif diaSemana == 'Thursday':
                diasSemana.append("Quinta")
            elif diaSemana == 'Friday':
                diasSemana.append("Sexta")
            elif diaSemana == 'Saturday':
                diasSemana.append("Sábado")
            else:
                diasSemana.append("Domingo")

        context['diasMes'] = listaDiasMes
        context['diasSemana'] = diasSemana

        diasMesSem = zip(listaDiasMes, diasSemana)
        context['diasMesSem'] = diasMesSem


        return context
