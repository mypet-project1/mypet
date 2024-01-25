import os
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db.models import Q

from config import settings
from accounts.models import User
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
            request.data["user"] = 2  # request.user.id 로 교체
            request.data["tip_media"] = request.FILES.getlist("tip_media")[0]
            new_tip = TipSerializers(data=request.data)

            if new_tip.is_valid():
                new_tip.save()

                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SerchTipAPIView(APIView):
    def get(self, request, word):
        if word:
            tips = Tip.objects.filter(
                Q(content__icontains=word)
                | Q(user__name__icontains=word)
                | Q(user__nickname__icontains=word)
            )

            serializer = TipSerializers(tips, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class OneTipAPIView(APIView):
    def get(self, request, animal, id):
        animal_id = get_object_or_404(Animal, name=animal)
        tip = get_object_or_404(Tip, id=id, animal=animal_id)
        serializer = TipSerializers(tip)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, animal, id):
        animal_id = get_object_or_404(Animal, name=animal)
        tip = get_object_or_404(Tip, id=id, animal=animal_id)

        if tip.tip_media:
            os.remove(os.path.join(settings.MEDIA_ROOT, tip.tip_media.path))

        request.data["user"] = 2  # request.user.id
        request.data["tip_media"] = request.FILES.getlist("tip_media")[0]
        serializer = TipSerializers(tip, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, animal, id):
        animal_id = get_object_or_404(Animal, name=animal)
        tip = get_object_or_404(Tip, id=id, animal=animal_id)

        if tip:
            tip.delete()

            return Response(status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
