from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from animals.models import Animal
from .models import Tip
from .serializers import TipSerializers


class TipAPIView(APIView):
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

    def post(self, request, animal):
        if Animal.objects.filter(name=animal).exists():
            request.data["user"] = 1  # request.user.id 로 교체
            request.data["tip_media"] = request.FILES.getlist("tip_media")[0]
            new_tip = TipSerializers(data=request.data)

            if new_tip.is_valid():
                new_tip.save()

                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
