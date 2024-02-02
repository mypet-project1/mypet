from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from accounts.models import User
from hospital.models import Hospital
from .models import HospitalChatRoom, Message
from .serializers import HospitalChatRoomSerializers, MessageSerializers


class HospitalChatRoomAPIView(APIView):
    def get(self, request, id):
        hospital = get_object_or_404(Hospital, id=id)
        chatroom = get_object_or_404(
            HospitalChatRoom, hospital=hospital, user=2
        )  # user=request.user 로 교체

        serializer = HospitalChatRoomSerializers(chatroom)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
