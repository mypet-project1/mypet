from django.db import models

from accounts.models import User
from hospital.models import Hospital


class HospitalChatRoom(models.Model):
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="chat_room"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hospital_chat_room"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["hospital"]),
            models.Index(fields=["user"]),
        ]

    def __str__(self):
        return f"{self.hospital} - {self.user} ChatRoom"


class Message(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message")
    chat_room = models.ForeignKey(
        HospitalChatRoom, on_delete=models.CASCADE, related_name="message"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["created_at"]),
            models.Index(fields=["sender"]),
            models.Index(fields=["chat_room"]),
        ]

    def __str__(self):
        return f"{self.chat_room} - {self.sender} Message"
