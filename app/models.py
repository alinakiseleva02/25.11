from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings

class UserWithPhone(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=15)

User = get_user_model()

class Service(models.Model):
    name = models.CharField('Название услуги', max_length=255)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Request(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    comment = models.TextField('Комментарий', blank=True, null=True)
    status = models.IntegerField(
        'Статус заявки',
        choices=[
            (0, 'Новая'),
            (1, 'Принята'),
            (2, 'Выполнена'),
        ],
        default=0
    )
    created_at = models.DateTimeField(
        "Дата создания", auto_now_add=True
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'