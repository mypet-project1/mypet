from django.urls import path

from . import views

app_name = "tips"
urlpatterns = [
    path("<str:animal>/", views.TipAPIView().as_view(), name="tips"),
    path("<str:animal>/<int:id>/", views.OneTipAPIView().as_view(), name="one_tip"),
]
