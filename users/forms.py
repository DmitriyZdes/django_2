from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

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


class ConfirmationCodeForm(forms.ModelForm):
    class Meta:
        fields = ('code',)

    def clean_code(self):
        code_qyeryset = ConfirmationCode.objects.filter(code_exact=self.cleaned_data.get('code'))

        if not code_qyeryset.exists():
            raise ValidationError('Введен неверный код')

        return self.cleaned_data['code']

class VerificationForm(forms.Form):
    verify_code = forms.CharField(max_length=12, label='Введите код верификации')
