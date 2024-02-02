from rest_framework import serializers

from .models import HospitalChatRoom, Message


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "chat_room", "sender", "message", "created_at"]


class HospitalChatRoomSerializers(serializers.ModelSerializer):
    message = MessageSerializers(many=True, read_only=True)

    class Meta:
        model = HospitalChatRoom
        fields = ["id", "hospital", "user", "message", "created_at"]
