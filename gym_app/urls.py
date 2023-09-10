from django.urls import path
from .views import GymApiView, UpdateGymApiView,GymApiView

urlpatterns = [
    path('gym/', GymApiView.as_view()),
    path('update/<int:pk>/', UpdateGymApiView.as_view()),
    path('filter/',GymApiView.as_view()),
]
