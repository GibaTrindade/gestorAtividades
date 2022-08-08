from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import GerarFrequencia


urlpatterns = [
    path('frequencia/<int:pk>', GerarFrequencia.as_view(), name='gerar_frequencia'),

]