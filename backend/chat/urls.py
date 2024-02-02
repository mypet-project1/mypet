from django.urls import path

from . import views

app_name = "chat"
urlpatterns = [
    path("<int:id>/", views.HospitalChatRoomAPIView.as_view(), name="chat_room")
]
