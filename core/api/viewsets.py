from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewset(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

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
    