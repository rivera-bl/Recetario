from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "App_core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Web Playground'})