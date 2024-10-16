from django.urls import path

from .views import LoginAPIView, RegisterAPIView, ValidateTokenAPIView

urlpatterns = [
    path('register/',RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('validate/', ValidateTokenAPIView.as_view())
]
