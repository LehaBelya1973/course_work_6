from datetime import timezone

from django.db import models


class MailingSettings(models.Model):
    start_date = models.DateTimeField(default=timezone.now, verbose_name='начало рассылки')
    finish_date = models.DateTimeField(verbose_name='конец рассылки')
    period = models.CharField() #сделать список для выбора периода
    status = models.CharField()  #сделать список для выбора статуса


class MailingLog(models.Model):
    last_date_time = models.DateTimeField(auto_now_add=True, verbose_name='дата последней отправки')
    status = models.CharField()  # сделать список для выбора статуса
    server_response = models.TextField(verbose_name='ответ почтового сервера')
    mailing = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='лог рассылки')
