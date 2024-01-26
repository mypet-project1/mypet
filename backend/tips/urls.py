from django.urls import path

from . import views

app_name = "tips"
urlpatterns = [
    path("<str:animal>/", views.TipAPIView().as_view(), name="tips"),
    path(
        "search/<str:word>/",
        views.SearchTipAPIView().as_view(),
        name="search_tips",
    ),
    path("<str:animal>/<int:id>/", views.OneTipAPIView().as_view(), name="one_tip"),
]
