from django.urls import path
from .views import PerfilPageView

urlpatterns = [
    path('perfil/', PerfilPageView.as_view(), name="perfil"),
]