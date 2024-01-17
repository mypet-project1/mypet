from .views import SignupAPIView

urlpatterns = [
    path("signup/", SignupAPIView.as_view()),
]
