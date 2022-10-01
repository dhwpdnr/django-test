from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, phone_number, password, is_staff, is_superuser, **extra_fields):
        if not phone_number:
            raise ValueError("user must have phone_number")
        now = timezone.now()
        user = self.model(
            phone_number=phone_number,
            is_active=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        if password:
            user.set_password(password) #암호화

        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password, **extra_fields):
        user = self._create_user(phone_number, password, False, False, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        user = self._create_user(phone_number, password, True, True, **extra_fields)
        user.username = f"admin-{user.id}"
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, phone_number):
        return self.get(phone_number=phone_number)

class User(AbstractUser):
    username = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.pk} {self.phone_number}"

    class Meta:
        db_table = "User"
