from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Tip
from .serializers import TipSerializers


class TipAllListAPIView(APIView):
    def get(self, request):
        tips = Tip.objects.all()
        serializer = TipSerializers(tips, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
