from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not any(char.islower() for char in password):
            raise ValidationError(_('Password must contain at least one lowercase letter.'))
        if not any(char.isupper() for char in password):
            raise ValidationError(_('Password must contain at least one uppercase letter.'))
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('Password must contain at least one digit.'))

    def get_help_text(self):
        return _(
            "Your password must contain at least one lowercase letter, "
            "one uppercase letter, and one digit."
        )
