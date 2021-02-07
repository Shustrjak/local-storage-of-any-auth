from django.db import models

# Create your models here.
class Storage(models.Model):
    place = models.CharField(max_length=255, verbose_name='Сайт:')
    login = models.CharField(max_length=255, verbose_name='Логин')
    passwd = models.CharField(max_length=255, verbose_name='Пароль')
    two_auth = models.BooleanField(default=False, verbose_name='Двухфакторная аутентификация')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):

        return self.place
