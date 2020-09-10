from django.urls import path
from .views import PerfilPageView, NuevaRecetaPageView

urlpatterns = [
    path('perfil/', PerfilPageView.as_view(), name="perfil"),
    path('nueva_receta/', NuevaRecetaPageView.as_view(), name="nueva_receta"),
]