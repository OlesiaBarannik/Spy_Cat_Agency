from rest_framework import viewsets
from .models import Target
from .serializers import TargetSerializer

class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
