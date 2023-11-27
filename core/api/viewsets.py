from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewset(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome','descricao','endereco__linha1')

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects

        if id:
            queryset.filter(pk=id)
        if nome:
            queryset.filter(nome__iexact=nome)
        if descricao:
            queryset.filter(descricao__iexact=descricao)

        
        return queryset
    