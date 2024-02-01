from django.urls import path

from . import views

app_name = "hospital"
urlpatterns = [
    path("list/", views.HospitalsAPIView.as_view(), name="hospital_list"),
    path("<int:id>/", views.OnehospitalAPIView.as_view(), name="one_hospital"),
]
