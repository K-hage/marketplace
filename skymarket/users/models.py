from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    choices = (
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор'),
    )


class User(AbstractBaseUser):
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    first_name = models.CharField(
        max_length=64,
        verbose_name='Имя',
        help_text='Введите имя, максимальное количество символов: 64'
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name='Фамилия',
        help_text='Введите фамилию, максимальное количество символов: 64'
    )
    phone = PhoneNumberField(
        max_length=128,
        verbose_name="Телефон для связи",
        help_text="Укажите телефон для связи",
    )
    email = models.EmailField(
        verbose_name='Email адрес',
        unique=True,
        help_text='Введите ваш email'
    )
    role = models.CharField(
        choices=UserRoles.choices,
        default=UserRoles.USER,
        max_length=15,
        verbose_name="Роль",
        help_text="Выберите роль пользователя",
    )
    image = models.ImageField(
        upload_to="photos/",
        verbose_name="Фото",
        help_text="Разместите Ваше фото",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="Аккаунт активен",
        help_text="Укажите, активен ли аккаунт"
    )

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
