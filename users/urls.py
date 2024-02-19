from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, ProfileView, VerifyEmailView, CustomPasswordResetView

app_name = UsersConfig.name

urlpatterns=[

    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('verify_email/<int:pk>/', VerifyEmailView.as_view(), name='verification'),
    path('pw_res/', CustomPasswordResetView.as_view(), name='password_new'),

]
