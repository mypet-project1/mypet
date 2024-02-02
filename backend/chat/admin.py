from django.contrib import admin

from .models import HospitalChatRoom, Message


@admin.register(HospitalChatRoom)
class HospitalChatRoomAdmin(admin.ModelAdmin):
    list_display = ["hospital", "user"]
    search_fields = ["hospital", "user"]
    ordering = ["hospital"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["chat_room", "sender", "message"]
    search_fields = ["chat_room", "sender", "message"]
    ordering = ["chat_room"]
