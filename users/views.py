from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView

from django.shortcuts import render

# Create your views here.


class LoginView(BaseLoginView):
    pass


class LogoutView(BaseLogoutView):
    pass
