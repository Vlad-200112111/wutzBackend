import profile

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(username, email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Platoon(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    STUDENT = 2
    TEACHER = 3
    EMPLOYEE = 4

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (EMPLOYEE, 'Employee'),
    )
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone = models.CharField(max_length=255, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        return self.role

    def __str__(self):
        return self.email


class New(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=1000)
    url_image = models.ImageField(upload_to="news/%Y-%m-%d/")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    html = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return self.name


class ElementsSlider(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=500)
    url_image = models.ImageField(upload_to="elements_slider/%Y-%m-%")

    def __str__(self):
        return self.name


class CategoriesForPage(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=500)
    html = models.TextField(max_length=1000000, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CategoriesForPage, on_delete=models.CASCADE)
    is_download = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MaterialsDistanceEducation(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE)
    url_image = models.ImageField(upload_to="materials/%Y-%m-%")

    def __str__(self):
        return self.name
