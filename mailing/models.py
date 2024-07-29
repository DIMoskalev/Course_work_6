from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='Почта')
    name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('email', 'name',)


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема письма')
    text = models.TextField(verbose_name='Тело письма')
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('title',)


class Mailing(models.Model):
    DAILY = 'Раз в день'
    WEEKLY = 'Раз в неделю'
    MONTHLY = 'Раз в месяц'

    PERIODIC_CHOICES = [
        (DAILY, 'Раз в день'),
        (WEEKLY, 'Раз в неделю'),
        (MONTHLY, 'Раз в месяц'),
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (CREATED, 'Создана'),
        (STARTED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]

    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default=CREATED, verbose_name='Статус')
    periodicity = models.CharField(max_length=150, choices=PERIODIC_CHOICES, default=DAILY,
                                   verbose_name='Периодичность')
    start_date = models.DateTimeField(verbose_name='Дата начала', **NULLABLE)
    end_date = models.DateTimeField(verbose_name='Дата окончания', **NULLABLE)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты для рассылки')

    def __str__(self):
        return f'{self.name}, статус:{self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('name',)


class Log(models.Model):
    time = models.DateTimeField(verbose_name='Дата и время последней попытки отправки')
    status = models.BooleanField(verbose_name='Статус попытки (успешно / не успешно')
    server_answer = models.CharField(max_length=150, verbose_name='Ответ почтового сервера',
                                     **NULLABLE)  # позже разобраться с фразой если он был, пока нулабл
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    def __str__(self):
        return f'{self.mailing} {self.time}, статус: {self.status}, ответ сервера: {self.server_answer}'

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылок'
