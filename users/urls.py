from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, ProfileView, VerifyEmailView, \
    ConfirmationCodeView, CustomPasswordResetView

app_name = UsersConfig.name

urlpatterns=[

    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('verify_email/', VerifyEmailView.as_view(), name='verify_email'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_confirm/', ConfirmationCodeView.as_view(), name='code_enter'),

]
