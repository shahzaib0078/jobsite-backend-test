"""Module contains models for accounts app."""

from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import UnicodeUsernameValidator

from base.models import Base, Parameter
from websites.models import Website


class UserAccount(AbstractUser, Parameter, Base):
    def __init__(self, *args, **kwargs) -> None:
        """Overriding username validators in AbstractUser object."""
        super(UserAccount, self).__init__(*args, **kwargs)
        self._meta.get_field("username").validators = [UnicodeUsernameValidator()]

    # Bio
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)

    # Status
    email_confirmed = models.BooleanField(default=False)

    # Foreign Key
    # website = models.ForeignKey(
    #     Website, on_delete=models.CASCADE
    # )
