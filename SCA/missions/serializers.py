from rest_framework import serializers
from .models import Mission
from targets.models import Target
from targets.serializers import TargetSerializer

class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True, read_only=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'complete', 'targets']

