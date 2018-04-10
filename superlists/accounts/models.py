from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=255)


class ListUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        return self.email == 'alvaro.camilloneto@gmail.com'

    @property
    def is_active(self):
        return True


class ListUserManager(BaseUserManager):

    def create_user(self, email):
        ListUser.objects.create(email=email)

    def create_superuser(self, email, password):
        self.create_user(email)