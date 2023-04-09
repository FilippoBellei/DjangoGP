from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

__all__ = ["Login", "Logout"]


class Login(LoginView):
    authentication_form = AuthenticationForm
    template_name = "authentication/login.html"
    next_page = "/"


class Logout(LogoutView):
    next_page = "/"
