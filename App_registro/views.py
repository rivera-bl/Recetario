from django.shortcuts import render
from django.views.generic.base import TemplateView


class RegistroPageView(TemplateView):
    template_name = "App_registro/registro.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Registro'})

class LoginPageView(TemplateView):
    template_name = "App_registro/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Login'})
