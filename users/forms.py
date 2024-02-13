from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from catalog.forms import StyleFormMixin
from users.models import User, ConfirmationCode
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


class ConfirmationCodeForm(forms.ModelForm):
    class Meta:
        model = ConfirmationCode
        fields = ('code',)

    def clean_code(self):
        code_qyeryset = ConfirmationCode.objects.filter(code_exact=self.cleaned_data.get('code'))

        if not code_qyeryset.exists():
            raise ValidationError('Введен неверный код')

        return self.cleaned_data['code']
