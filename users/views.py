from django.views import generic
from .models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse
from django.http import HttpResponseRedirect


class ProfileView(generic.DetailView):
    """ View para o perfil de usuário """

    template_name = 'users/profile.html'
    model = User


class LogoutView(LogoutView):
    next_page = 'common:home'


class LoginView(LoginView):
    success_url = 'common:home'
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:home'))
        return super(LoginView, self).get(request)

