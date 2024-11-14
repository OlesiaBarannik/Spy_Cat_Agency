from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Mission
from .serializers import MissionSerializer
from targets.models import Target
from targets.serializers import TargetSerializer

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def create(self, request, *args, **kwargs):
        mission_data = request.data
        targets_data = mission_data.pop('targets', [])

        mission_serializer = MissionSerializer(data=mission_data)
        if mission_serializer.is_valid():
            mission = mission_serializer.save()

            for target_data in targets_data:
                target_data['mission'] = mission.id  # Прив'язуємо цілі до створеної місії
                target_serializer = TargetSerializer(data=target_data)
                if target_serializer.is_valid():
                    target_serializer.save()
                else:
                    return Response(target_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(mission_serializer.data, status=status.HTTP_201_CREATED)
        return Response(mission_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        missions = Mission.objects.all()
        serializer = self.get_serializer(missions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            mission = self.queryset.get(id=pk)
            serializer = MissionSerializer(mission)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Mission.DoesNotExist:
            return Response(
                {"error": "Mission not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk=None, partial=False):
        try:
            mission = self.queryset.get(id=pk)
        except Mission.DoesNotExist:
            return Response({"error": "Mission not found"}, status=status.HTTP_404_NOT_FOUND)

        if mission.complete and 'notes' in request.data:
            return Response(
                {"error": "Cannot update notes for a completed mission"},
                status=status.HTTP_400_BAD_REQUEST
            )

        mission_serializer = MissionSerializer(mission, data=request.data, partial=partial)
        if mission_serializer.is_valid():
            updated_mission = mission_serializer.save()

            targets_data = request.data.get('targets', [])
            for target_data in targets_data:
                try:
                    target = Target.objects.get(id=target_data.get('id'), mission=updated_mission)
                    if target.complete and 'notes' in target_data:
                        return Response(
                            {"error": "Cannot update notes for a completed target"},
                            status=status.HTTP_400_BAD_REQUEST
                        )

                    target_serializer = TargetSerializer(target, data=target_data, partial=True)
                    if target_serializer.is_valid():
                        target_serializer.save()
                    else:
                        return Response(target_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except Target.DoesNotExist:
                    return Response(
                        {"error": f"Target with id {target_data.get('id')} not found"},
                        status=status.HTTP_404_NOT_FOUND
                    )

            return Response(mission_serializer.data, status=status.HTTP_200_OK)
        return Response(mission_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            mission = self.queryset.get(id=pk)
        except Mission.DoesNotExist:
            return Response({"error": "Mission not found"}, status=status.HTTP_404_NOT_FOUND)

        if mission.cat is not None:
            return Response(
                {"error": "Cannot delete a mission assigned to a cat"},
                status=status.HTTP_400_BAD_REQUEST
            )

        mission.delete()
        return Response({"message": "Mission deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
