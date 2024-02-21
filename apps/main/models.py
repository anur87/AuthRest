from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime


class UserManager(BaseUserManager):
    def create(self, **extra_fields):
        return self.create_user(**extra_fields)


    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email must be provided!')
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(**extra_fields)

       
    
class User(AbstractUser):
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True)
    birth_day = models.DateField()
    email_confirmed = models.BooleanField(default=False)

    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'birth_day']  
    
    @property
    def age(self):
        today = datetime.now().date()
        return (today - self.birth_day).days // 365
