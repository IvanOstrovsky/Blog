from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import RegisterUserForm, LoginForm, UserProfileForm
from users.models import User


class RegisterView(TitleMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    title = 'Регистрация'
    success_url = reverse_lazy('users:login')


class LoginUserView(TitleMixin, LoginView):
    form_class = LoginForm
    title = 'Авторизация'
    template_name = 'users/login.html'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=self.object.id)
