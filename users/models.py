""" User model """

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    """ User model.
    Extend from Django's Abstract User, change the mobile_phone field
    to email and add some extra fields.
    """
    username = models.CharField(max_length=70, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    mobile_phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        })
    USERNAME_FIELD = 'mobile_phone'
    date_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    session_active = models.BooleanField('client', default=True,)
