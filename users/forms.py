from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.forms import StyleFormMixin
from users.models import User
from django import forms

class UserForm(StyleFormMixin, UserCreationForm):

    class Meta:

        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'phone_number', 'country', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
