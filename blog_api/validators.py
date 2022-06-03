from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.translation import ngettext


class FullCommonValidator:
    """
    Validate whether the password is of a minimum length = 8.
    Validate whether the password has more than 1 digit.
    Validate whether the password has more than 1 letter.
    """

    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "This password is too short. It must contain at least "
                    "%(min_length)d character.",
                    "This password is too short. It must contain at least "
                    "%(min_length)d characters.",
                    self.min_length,
                ),
                code="password_too_short",
                params={"min_length": self.min_length},
            )

        alpha_check = False
        digit_check = False
        for symbol in password:
            if symbol.isdigit():
                digit_check = True
            if symbol.isalpha():
                alpha_check = True

        if not alpha_check or not digit_check:
            raise ValidationError(
                _("This password is contain only from digits or letters"),
                code="password_only_with_letters_or_digits",
            )

    def get_help_text(self):
        return ngettext(
            "Your password must contain at least %(min_length)d character.",
            "Your password must contain at least %(min_length)d characters.",
            self.min_length,
        ) % {"min_length": self.min_length}, \
               _("Your password must contain at least one digit and one letter.")
