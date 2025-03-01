from django.db import models
from auth_profile.user_manager import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from common.mixins import TimeStampMixin
from uuid import uuid4


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    
    email = models.EmailField(
        max_length=255,
        unique=True,
        error_messages={
            'unique': "A user with that email already exists.",
        },
    )
    
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        error_messages={
            'unique': "A user with that phone number already exists.",
        },
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
        verbose_name='active',
    )
    
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.',
        verbose_name='staff status',
    )
    
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='date joined',
    )
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']
    
    def __str__(self):
        return self.email or self.phone_number
    
    
class Seller(TimeStampMixin):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    
    first_name = models.CharField(
        max_length=255,
        verbose_name='first name',
    )
    
    last_name = models.CharField(
        max_length=255,
        verbose_name='last name',
    )
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='seller',
        verbose_name='user',
    )
    
    store = models.OneToOneField(
        'Store',
        on_delete=models.CASCADE,
        related_name='seller',
        verbose_name='store',
    )
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Buyer(TimeStampMixin):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    
    first_name = models.CharField(
        max_length=255,
        verbose_name='first name',
    )
    
    last_name = models.CharField(
        max_length=255,
        verbose_name='last name',
    )
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='buyer',
        verbose_name='user',
    )
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    

class Address(TimeStampMixin):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    
    province = models.CharField(
        max_length=255,
        verbose_name='province',
    )
    
    district = models.CharField(
        max_length=255,
        verbose_name='district',
    )
    
    landmark = models.CharField(
        max_length=255,
        verbose_name='landmark',
    )
    
    municipality = models.CharField(
        max_length=255,
        verbose_name='municipality',
    )
    
    tole = models.CharField(
        max_length=255,
        verbose_name='tole',
    )
    
    is_main = models.BooleanField(
        default=False,
        verbose_name='main address',
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name='user',
    )
    
    def __str__(self):
        return f'{self.province}, {self.district}, {self.municipality}, {self.tole}'
    
    

class Store(TimeStampMixin):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    
    name = models.CharField(
        max_length=255,
        verbose_name='name',
    )
    
    description = models.TextField(
        verbose_name='description',
    )
    
    rating = models.FloatField(
        default=0.0,
        verbose_name='rating',
    )
    
    def __str__(self):
        return self.name