from django.shortcuts import render
from django.views.generic.base import TemplateView

class PerfilPageView(TemplateView):
    template_name = "App_perfil_usuario/perfil.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Perfil'})