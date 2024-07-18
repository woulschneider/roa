from django.db import models

class AtendimentoMedico(models.Model):
    nome_paciente = models.CharField(max_length=100)
    data_atendimento = models.DateTimeField(auto_now_add=True)
    primeira_avaliacao = models.BooleanField(default=True)
    cid = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome_paciente} - {self.data_atendimento}"

    class Meta:
        ordering = ['-data_atendimento']