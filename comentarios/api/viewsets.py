from rest_framework.viewsets import ModelViewSet
from ..models import Comentario
from .serializers import ComentarioSerializer

class ComentariosViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer