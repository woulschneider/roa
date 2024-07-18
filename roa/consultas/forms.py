from django import forms
from .models import AtendimentoMedico

class AtendimentoMedicoForm(forms.ModelForm):
    class Meta:
        model = AtendimentoMedico
        fields = ['nome_paciente', 'primeira_avaliacao', 'cid']
        labels = {
            'nome_paciente': 'Nome do Paciente',
            'primeira_avaliacao': 'Primeira Avaliação',
            'cid': 'CID (Diagnóstico)'
        }
        widgets = {
            'primeira_avaliacao': forms.RadioSelect(choices=[(True, 'Sim'), (False, 'Não')])
        }