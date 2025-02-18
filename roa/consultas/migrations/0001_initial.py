# Generated by Django 5.0.7 on 2024-07-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtendimentoMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_paciente', models.CharField(max_length=100)),
                ('data_atendimento', models.DateTimeField(auto_now_add=True)),
                ('primeira_avaliacao', models.BooleanField(default=True)),
                ('cid', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-data_atendimento'],
            },
        ),
    ]
