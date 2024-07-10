import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def username_validator(username):
    pattern = r''
    if not re.match(pattern, username):
        raise ValidationError(_("Username is invalid"), code='invalid')
    return username


def image_validator(image):
    if image:
        if not image.name.endswith('.png'):
            raise ValidationError(_("Image is invalid"), code='invalid')
    return image


def password_validator(password):
    pattern = r''
    if not re.match(pattern, password):
        raise ValidationError(_("Password is invalid"), code='invalid')
    return password
