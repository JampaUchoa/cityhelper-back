# serializers.py
from rest_framework import serializers, viewsets
from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer
import requests
from .models import Solicitation
from django.db.models import Max
from datetime import datetime

class SolicitationSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Solicitation
        fields = '__all__'

    def create(self, validated_data):
        
        solicitation = Solicitation(**validated_data)
        solicitation.processo_status = "aberto"
        solicitation.solicitacao_data = datetime.now()
        solicitation.save()
        return solicitation

    def to_internal_value(self, data):
        data["processo_numero"] = Solicitation.objects.aggregate(Max('processo_numero'))["processo_numero__max"] + 1

        return super(SolicitationSerializer, self).to_internal_value(data)


# class UserSerializer(serializers.ModelSerializer):
#     token = serializers.UUIDField(required=False)

#     class Meta:
#         model = User
#         fields = ('email', 'password', 'name', 'token')
#         extra_kwargs = {
#             'password': {'write_only': True},
#             'token': {'write_only': True}
#         }

#     def validate(self, data):
#         user_qs = User.objects.filter(username__iexact=data["email"])
#         if not data["email"]:
#             raise ValidationError({'email': ["O campo email não pode ficar em branco!."]})
#         if user_qs.exists() and user_qs.count() == 1:
#             raise ValidationError({'error': "Usuário já existe!"})
#         return data

#     def create(self, validated_data):
#         token = None
#         if validated_data.get('token'):
#             token = validated_data.pop('token')
#         password = validated_data.pop('password')
#         validated_data['username'] = validated_data['email']
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()

#         return user

