from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from user_app.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Форма для регистрации нового пользователя."""
    email = forms.EmailField(
        required=True,
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}),
    )

    class Meta:
        model = get_user_model()
        fields = ('email',)

        def clean_email(self):
            email = self.cleaned_data['email'].lower()
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Этот email уже занят.')
            return email


class CustomAuthenticationForm(AuthenticationForm):
    """Форма для входа пользователя по email."""

    username = forms.EmailField(
        required=True,
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}),
    )

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        return username


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')

        def clean_email(self):
            email = self.cleaned_data.get('email').lower()
            if CustomUser.objects.filter(email=email).exists():
                raise forms.ValidationError('Пользователь с таким email уже есть')
            return email