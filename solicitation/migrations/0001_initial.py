# Generated by Django 3.1.5 on 2021-02-07 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processo_numero', models.IntegerField(null=True, verbose_name='Numero de processo')),
                ('solicitacao_data', models.DateTimeField(null=True, verbose_name='Data da solicitação')),
                ('solicitacao_descricao', models.TextField(null=True, verbose_name='Descrição')),
                ('solicitacao_regional', models.TextField(null=True, verbose_name='Região')),
                ('solicitacao_bairro', models.TextField(null=True, verbose_name='Bairro')),
                ('solicitacao_localidade', models.TextField(null=True)),
                ('solicitacao_endereco', models.TextField(null=True)),
                ('solicitacao_roteiro', models.TextField(null=True)),
                ('rpa_codigo', models.IntegerField(null=True)),
                ('rpa_nome', models.TextField(null=True)),
                ('solicitacao_microrregiao', models.TextField(null=True)),
                ('solicitacao_plantao', models.TextField(null=True)),
                ('solicitacao_origem_chamado', models.TextField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('solicitacao_vitimas', models.BooleanField(null=True)),
                ('solicitacao_vitimas_fatais', models.BooleanField(null=True)),
                ('processo_situacao', models.TextField(null=True)),
                ('processo_tipo', models.TextField(null=True)),
                ('processo_origem', models.TextField(null=True)),
                ('processo_localizacao', models.TextField(null=True)),
                ('processo_data_conclusao', models.DateTimeField(null=True)),
            ],
        ),
    ]
