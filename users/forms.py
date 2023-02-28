from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User


class UsersUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "name", "dob"]


class UsersUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email"]
