# Model mixins

from django.core.validators import RegexValidator
from django.db import models


class Addressable(object):
    ADDRESS_MAX_LENGTH = 250
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH)


class Commentable(object):
    COMMENT_MAX_LENGTH = 100
    comment = models.CharField(max_length=COMMENT_MAX_LENGTH)


class Phonable(object):
    phone_regex = RegexValidator(regex=r'^\+?\d{9,15}$', message="Up to 15 digits allowed in format +123456789.")
    phone_number = models.CharField(validators=[phone_regex], blank=True)


class Pricable(object):
    PRICE_MAX_DIGITS = 7
    price = models.DecimalField(decimal_places=2, max_digits=PRICE_MAX_DIGITS)
