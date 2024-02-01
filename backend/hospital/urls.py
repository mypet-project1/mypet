from django.urls import path

from . import views

app_name = "hospital"
urlpatterns = [
    path("", views.HospitalsAPIView.as_view(), name="hospital_list"),
    path("<int:id>/", views.OneHospitalAPIView.as_view(), name="one_hospital"),
    path("<int:id>/review/", views.ReviewAPIView.as_view(), name="review"),
    path("review/<int:id>/", views.OneReviewAPIView.as_view(), name="one_review"),
]
