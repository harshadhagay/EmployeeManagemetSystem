from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from account.models import Manager

# Create your models here.
class Employee(models.Model):
    '''
     Employee model database table 
     
    '''
    manager = models.ForeignKey(Manager,
                            on_delete = models.CASCADE,
                            related_name='manager_employee',
                            )
    
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
    city = models.CharField(max_length = 100)
    phone_regex = RegexValidator(regex = r'^\+?1?\d{9,15}$',message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed')
    phonenumber = models.CharField(validators=[phone_regex], max_length=17, blank=True) #validators should be list
    
    def __str__(self):
        return self.firstname
    