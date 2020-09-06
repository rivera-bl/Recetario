from django.shortcuts import render
from django.views.generic.base import TemplateView


class BusquedaRecetasPageView(TemplateView):
    template_name = "App_recetas/busqueda_recetas.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Recetas'})

class RecetaPageView(TemplateView):
    template_name = "App_recetas/receta.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Receta'})