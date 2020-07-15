from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager

class Manager(AbstractBaseUser,PermissionsMixin):
    '''
    Manager model database table
    
    '''
    
    email = models.EmailField(_('email address'), 
                              unique=True)
    firstname = models.CharField(max_length=100,
                                 null = True,
                                 blank= True)
    lastname = models.CharField(max_length=100,
                                null = True,
                                 blank= True)
    address = models.CharField(max_length=200,
                                null = True
                                )
    date_of_birth = models.DateField(null = True)
    company = models.CharField(max_length=100,
                               null=True,
                               blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname']
    
    #Django that the CustomUserManager class defined in managers.py should manager
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'manager'
        verbose_name_plural = 'managers'