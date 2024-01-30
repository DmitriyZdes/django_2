from random import randint

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView, \
    PasswordResetView


from django.core.mail import send_mail
from django.http import HttpResponseForbidden

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserForm, UserProfileForm
from users.models import User

# Create your views here.


class LoginView(BaseLoginView):

    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass

class RegisterView(CreateView):

    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        new_user = form.save()
        mail_subject = 'Рады, что вы нашли именно нас!'
        message = 'Поздравляем, Вы зарегистрировались на нашем портале!'

        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return response

class VerifyEmailView(View):
    def get(self, request, uid, token):
        try:
            user = get_object_or_404(User, pk=uid, verification_token=token)
            user.is_verified = True
            user.save()
            return render(request, 'users/registration_success.html')
        except User.DoesNotExist:
            return render(request, 'users/registration_failed.html')

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:user_form')

    def get_object(self, queryset=None):
        return self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_verified:
            return HttpResponseForbidden("Ваша электронная почта еще не проверена.")
        return super().dispatch(request, *args, **kwargs)


class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        # Генерация нового случайного пароля
        new_password = ''.join([str(randint(0, 9)) for _ in range(12)])
        email = form.cleaned_data['email']
        User = get_user_model()
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.save()

        send_mail(
            subject='Восстановление пароля',
            message=f'Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        return super().form_valid(form)
