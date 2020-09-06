from django.urls import path
from .views import RegistroPageView, LoginPageView

urlpatterns = [
    path('registro/', RegistroPageView.as_view(), name="registro"),
    path('login/', LoginPageView.as_view(), name="login"),
]