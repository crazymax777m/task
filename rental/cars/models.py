from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

LANGUAGES = [
    ('RU', 'Russian'),
    ('ENG', 'English'),
]


class Car(models.Model):
    name = models.CharField(_('Название'), max_length=120)
    year_creation = models.PositiveIntegerField('Год создания')
    date_add = models.DateField('Дата добавления машины в систему', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class CustomUser(AbstractUser):
    language = models.CharField('Язык', max_length=50, choices=LANGUAGES)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, null=True)


# class Person(models.Model):
#     email = models.EmailField('Email', unique=True)
#     name = models.CharField('Имя', max_length=120)
#     language = models.CharField('Язык', max_length=120, choices=LANGUAGES)
#     cars = models.ManyToManyField(Car, verbose_name='Машины')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
