from django.views import generic
from django.contrib import auth
from django.contrib.auth import get_user_model, authenticate, views
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .models import User
from .forms import UserForm


class ProfileView(generic.DetailView):
    """ View para o perfil de usuário """

    template_name = 'users/profile.html'
    model = User


class LogoutView(views.LogoutView):
    next_page = 'common:home'


class LoginView(views.LoginView):
    success_url = 'common:home'
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:home'))
        return super(LoginView, self).get(request)


class SignupView(generic.FormView):
    form_class = UserForm
    success_url = 'users:login'
    template_name = 'users/signup.html'
    redirect_authenticated_user = True

    model = get_user_model()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:home'))
        return super(SignupView, self).get(request)

    def form_valid(self, form):
        self.object = form.save()
        user = authenticate(username=self.object.email,
                            password=form.cleaned_data['password'])
        auth.login(self.request, user)

        return redirect('common:home')
