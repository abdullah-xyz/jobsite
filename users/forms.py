from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UsersUserCreationForm(UserCreationForm):
    dob = forms.DateField(
        required=True,
        # to_field_name="dob",
        label="Date of Birth",
        widget=forms.DateInput(attrs={"type": "date", "class": "input"}),
    )

    email = forms.EmailField(
        required=True, label="Email", widget=forms.EmailInput(attrs={"class": "input"})
    )

    name = forms.CharField(
        required=True, label="Name", widget=forms.TextInput(attrs={"class": "input"})
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "input"}
        ),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "input"}
        ),
        strip=False,
    )

    class Meta:
        model = User
        fields = ["email", "name", "dob"]


class UsersUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email"]
