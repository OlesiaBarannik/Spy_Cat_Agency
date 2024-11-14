from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Cat
from .serializers import CatSerializer

class CatViewSet(viewsets.ViewSet):
    queryset = Cat.objects.all()

    def list(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            cat = self.queryset.get(id=pk)
            serializer = CatSerializer(cat)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cat.DoesNotExist:
            return Response(
                {"error": "Cat not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def create(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Cat created successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            cat = self.queryset.get(id=pk)
            serializer = CatSerializer(cat, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Cat updated successfully"}, status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Cat.DoesNotExist:
            return Response(
                {"error": "Cat not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def destroy(self, request, pk=None):
        try:
            cat = self.queryset.get(id=pk)
            cat.delete()
            return Response(
                {"message": "Cat deleted successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        except Cat.DoesNotExist:
            return Response(
                {"error": "Cat not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
