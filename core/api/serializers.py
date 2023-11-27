from ..models import PontoTuristico
from rest_framework.serializers import ModelSerializer

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id','nome','descricao','status', 'foto', 'atracoes','comentarios','avaliacoes','endereco')