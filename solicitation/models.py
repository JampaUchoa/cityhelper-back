from django.db import models
from django.conf import settings


class Solicitation(models.Model):

    processo_numero = models.BigIntegerField("Numero de processo", null=False, unique=True)
    solicitacao_data = models.DateTimeField("Data da solicitação", null=True)
    solicitacao_descricao = models.TextField("Descrição", null=True)
    solicitacao_regional = models.TextField("Região", null=True)
    solicitacao_bairro = models.TextField("Bairro", null=True)
    solicitacao_localidade = models.TextField(null=True)
    solicitacao_endereco = models.TextField(null=True)
    solicitacao_roteiro = models.TextField(null=True)

    rpa_codigo = models.IntegerField(null=True)
    rpa_nome = models.TextField(null=True)

    solicitacao_microrregiao = models.TextField(null=True)
    solicitacao_plantao = models.BooleanField(null=True)
    solicitacao_origem_chamado = models.TextField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    solicitacao_vitimas = models.BooleanField(null=True)
    solicitacao_vitimas_fatais = models.BooleanField(null=True)
    processo_situacao = models.TextField(null=True)
    processo_tipo = models.TextField(null=True)
    processo_origem = models.TextField(null=True)
    processo_localizacao = models.TextField(null=True)
    processo_status = models.TextField(null=True)
    processo_data_conclusao = models.DateTimeField(null=True)
