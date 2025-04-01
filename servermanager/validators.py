from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class SpecialCharacterCheckValidator:
    def __init__(self, char_count=1, special_characters="!@#$%^&*()_+-=,.<>?:;\'\"[{]}\\|"):
        self.char_count = char_count
        self.special_characters = special_characters

    def validate(self, password, user=None):
        special_character_count = [char for char in password if char in self.special_characters]
        if len(special_character_count) < self.char_count:
            raise ValidationError(
                _("Your password must contain at least %(char_count)d special character(s)."),
                code='invalid_password',
                params={'char_count': self.char_count},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(char_count)d special character(s)."
            % {'char_count': self.char_count}
        )