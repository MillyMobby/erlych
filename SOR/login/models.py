from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.mail import send_mail
#from django.urls import reverse 
#from django_countries.fields import CountryField

class AccountManager(BaseUserManager):

    def create_superuser(self, email, username, password, **other):

        other.setdefault('is_staff', True)
        other.setdefault('is_superuser', True)
        other.setdefault('is_active', True) 
        return self.create_account(email, username, password, **other)
    

    def create_account(self, email, username, password, **other):

        if not email:
            raise ValueError(('Devi inserire un indirizzo email'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **other)
        user.set_password(password)
        user.save()
        return user



class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=60, unique=True)
    
    # User Status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    #created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'l@1.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.username

 
