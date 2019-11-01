from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):
        now = timezone.now()
        if not request_data['username']:
            raise ValueError('Users must have an username.')
        profile = ""
        if request_data.get('profile'):
            profile = request_data['profile']
        email = ""
        if request_data.get('email'):
            email= request_data['email']
        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(email),
            is_active=True,
            last_login=now,
            date_joined=now,
            profile=profile
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        request_data = {
            'username': username,
            'email': email,
            'password': password
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username    = models.CharField(_('username'), max_length=30, unique=True)
    first_name  = models.CharField(_('first name'), max_length=30, blank=True)
    last_name   = models.CharField(_('last name'), max_length=30, blank=True)
    email       = models.EmailField(verbose_name='email address', max_length=255, blank=True)
    profile     = models.CharField(_('profile'), max_length=255, blank=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = AccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def user_has_perm(self, perm, obj):
        return _user_has_perm(self, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_short_name(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = 'api_user'
        swappable = 'AUTH_USER_MODEL'

class PostData(models.Model):
    purpose = models.CharField(max_length=16)
    message = models.TextField()
    pic = models.ImageField(upload_to='photo', null=True)
    post_time = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    lat = models.DecimalField(u'緯度', max_digits=11, decimal_places=8, default=0)
    lng = models.DecimalField(u'経度', max_digits=11, decimal_places=8, default=0)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return self.purpose