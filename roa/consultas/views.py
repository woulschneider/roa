from django.shortcuts import render, redirect
from .models import AtendimentoMedico
from .forms import AtendimentoMedicoForm
from django.utils import timezone

def lista_atendimentos(request):
    atendimentos = AtendimentoMedico.objects.all()
    return render(request, 'consultas/lista_atendimentos.html', {'atendimentos': atendimentos})

def novo_atendimento(request):
    if request.method == 'POST':
        form = AtendimentoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_atendimentos')
    else:
        form = AtendimentoMedicoForm()
    return render(request, 'consultas/novo_atendimento.html', {'form': form})

def imprimir_lista_dia(request):
    hoje = timezone.now().date()
    atendimentos_do_dia = AtendimentoMedico.objects.filter(data_atendimento__date=hoje).order_by('data_atendimento')
    return render(request, 'consultas/imprimir_lista_dia.html', {'atendimentos': atendimentos_do_dia, 'data': hoje})