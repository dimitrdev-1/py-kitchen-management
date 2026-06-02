from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
            "email",
        )
