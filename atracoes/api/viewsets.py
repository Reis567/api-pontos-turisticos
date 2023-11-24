from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Atracao
from .serializers import AtracaoSerializer

class AtracaoViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('nome', 'descricao')
