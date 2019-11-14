from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

    
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    username= models.CharField(max_length=30, unique=False)
    is_staff = models.BooleanField(_('staff status'),default=False)
    is_active = models.BooleanField(_('active'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
