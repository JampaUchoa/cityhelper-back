from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.conf import settings
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
import csv
import datetime

from .serializers import *
from .models import *

# Solicitation
class SolicitationViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitationSerializer
    model = Solicitation
    queryset = Solicitation.objects.all()


class LoadCSV(APIView):

    def get(self, request):
        fields = [
            "_id",
            "ano",
            "mes",
            "processo_numero",
            "solicitacao_data",
            "solicitacao_hora",
            "solicitacao_descricao",
            "solicitacao_regional",
            "solicitacao_bairro",
            "solicitacao_localidade",
            "solicitacao_endereco",
            "solicitacao_roteiro",
            "rpa_codigo",
            "rpa_nome",
            "solicitacao_microrregiao",
            "solicitacao_plantao",
            "solicitacao_origem_chamado",
            "latitude",
            "longitude",
            "solicitacao_vitimas",
            "solicitacao_vitimas_fatais",
            "processo_situacao",
            "processo_tipo",
            "processo_origem",
            "processo_localizacao",
            "processo_status",
            "processo_data_conclusao"
        ]

        with open('seed.csv') as csvfile:
            filereader = csv.reader(csvfile)
            for row in filereader:

                res = dict(zip(fields, row))

                #Convert to bool
                res["solicitacao_plantao"] = (res["solicitacao_plantao"] == "Sim")
                res["solicitacao_vitimas"] = (res["solicitacao_vitimas"] == "Sim")
                res["solicitacao_vitimas_fatais"] = (res["solicitacao_vitimas_fatais"] == "Sim")
                del res["_id"]
                del res["ano"]
                del res["mes"]

                solicitacao_dt = datetime.datetime.strptime(res["solicitacao_data"], '%Y-%m-%dT%H:%M:%S')
                horas = res["solicitacao_hora"].split(":")
                res["solicitacao_data"] = solicitacao_dt.replace(hour=int(horas[0]), minute=int(horas[1]))

                del res["solicitacao_hora"]

                if not isinstance(res["latitude"], float):
                    del res["latitude"]
                    del res["longitude"]

                if not res["processo_data_conclusao"]:
                    del res["processo_data_conclusao"]

                if res["rpa_codigo"] == "Não informada":
                    del res["rpa_codigo"]
                try:
                    new_solicitation = Solicitation.objects.update_or_create(processo_numero=res["processo_numero"], defaults=res)
                except Exception as e: 
                    print(e)
                    print(res)
                    break

        return Response(status=204)
