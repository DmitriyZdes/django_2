import random

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView, \
    PasswordResetView
from django.urls import reverse

from django.core.mail import send_mail
from django.http import HttpResponseForbidden

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, FormView

from users.forms import UserForm, UserProfileForm, VerificationForm
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
        user = form.save(commit=False)
        user.is_active = False
        generate_code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        user.verify_code = generate_code
        user.save()
        mail_subject = 'Рады, что вы нашли именно нас!'
        message = f'Поздравляем, Вы зарегистрировались на нашем портале! Для верификации аккаунта введите код {generate_code}'

        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        return redirect(reverse('users:verification', kwargs={'pk': user.pk}))

class VerifyEmailView(View):

    template_name = 'users/verification.html'
    def get(self, request, *args, **kwargs):
        form = VerificationForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = VerificationForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['verify_code']
            user_pk = kwargs.get('pk')
            user = get_object_or_404(User, pk=user_pk)
            if entered_code == user.verify_code:
                user.is_active = True
                user.save()
                messages.success(request, 'Аккаунт успешно активирован!')
                return redirect(reverse('users:login'))
            else:
                messages.error(request, 'Неверный код верификации. Попробуйте снова.')

            return render(request, self.template_name, {'form': form})

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
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
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


class SuccessConfirmationMixin:
    def form_valid(self, form):

        code = form.cleaned_data.get('code')
        user = (
            User.objects.filter(confirmation_code=code).select_related('confirmation_code').first()


        )
        user.is_active=True
        user.confirmation_code.delete()
        user.save()
        login(self.request, user)
        return super().form_valid(form)


class ConfirmationCodeView(FormView):

        success_url = reverse_lazy('users:login')
        template_name = 'users/password_confirm_email.html'
