from django.urls import path

from . import views

app_name = "tips"
urlpatterns = [
    path("all/", views.TipAllListAPIView().as_view(), name="tips"),
]
