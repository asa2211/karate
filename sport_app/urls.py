from django.urls import path
from .views import SignUpApiView

urlpatterns = [
    path('sign_up/', SignUpApiView.as_view()),
]
