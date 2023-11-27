from ..models import PontoTuristico
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    class Meta:
        model = PontoTuristico
        fields = ('id','nome','descricao','status', 'foto', 'atracoes','comentarios','avaliacoes','endereco')