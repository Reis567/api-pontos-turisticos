from ..models import PontoTuristico
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    class Meta:
        model = PontoTuristico
        fields = ('id','nome','descricao','status', 'foto', 'atracoes','comentarios','avaliacoes','endereco')