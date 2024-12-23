from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to find the user by email or username
            user = User.objects.get(Q(username=username) | Q(email__iexact=username))
        except User.DoesNotExist:
            return None

        # Check if the password is valid
        if user.check_password(password):
            return user

        return None