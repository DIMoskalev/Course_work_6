from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('email', 'name',)


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема письма')
    text = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('title',)


class Mailing(models.Model):
    pass


class Log(models.Model):
    pass
