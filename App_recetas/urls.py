from django.urls import path
from .views import BusquedaRecetasPageView, RecetaPageView

urlpatterns = [
    path('recetas/', BusquedaRecetasPageView.as_view(), name="recetas"),
    path('receta/', RecetaPageView.as_view(), name="receta"),
]