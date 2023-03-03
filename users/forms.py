from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UsersUserCreationForm(UserCreationForm):
    dob = forms.DateField(
        required=True,
        # to_field_name="dob",
        label="Date of Birth",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = User
        fields = ["email", "name", "dob"]


class UsersUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email"]
