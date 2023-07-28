from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomPasswordValidator:

    def validate(self, password, user=None):
        if len(password) > 24:
            raise ValidationError(_('Password must be at most 24 characters long.'))