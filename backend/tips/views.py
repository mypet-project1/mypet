from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from animals.models import Animal
from .models import Tip
from .serializers import TipSerializers


class TipAllListAPIView(APIView):
    def get(self, request, animal):
        if Animal.objects.filter(name=animal).exists():
            animal_id = get_object_or_404(Animal, name=animal)
            tips = Tip.objects.filter(animal=animal_id)
        elif animal == "all":
            tips = Tip.objects.all()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = TipSerializers(tips, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
