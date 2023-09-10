from django.urls import path
from .views import AllTrenerView

urlpatterns = [
    path('all/', AllTrenerView.as_view())
]
