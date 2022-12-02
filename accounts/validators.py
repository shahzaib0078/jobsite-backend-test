"""Module contains validators for accounts app."""

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r"^[\w!&.@+-]+\Z"
    message = _(
        "Enter a valid username. This field only contains letters, "
        "numbers, and @/./+/-/_/!/& characters."
    )
    flags = 0
