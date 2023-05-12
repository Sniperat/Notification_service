from django.db import models
from django.core.validators import RegexValidator
import pytz
from django.utils import timezone

utc = pytz.UTC


class CodeMobileOperatorModel(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = 'Код мобильного оператора'
        verbose_name_plural = 'Код мобильного оператора'


class TagModel(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class ClientModel(models.Model):
    phone_regex = RegexValidator(regex=r'^(7)\d{10}$',
                                 message="Phone number must be entered in the format: '7XXXXXXXXX'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11)
    code_mobile_operator = models.ForeignKey(CodeMobileOperatorModel, on_delete=models.RESTRICT, related_name='clients')
    tag = models.ForeignKey(TagModel, on_delete=models.RESTRICT, related_name='clients', null=True, blank=True)
    timezone = models.CharField(max_length=10)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенти'


class MessageModel(models.Model):
    class Status(models.TextChoices):
        WAITING = 'Waiting'
        SENT = 'Sent'
        FAILED = 'Failed'

    send_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.WAITING)
    mail = models.ForeignKey('MailModel', models.RESTRICT, related_name='messages')
    client = models.ForeignKey('ClientModel', models.RESTRICT, related_name='messages')

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailModel(models.Model):
    start_date = models.DateTimeField()
    text = models.TextField()
    end_date = models.DateTimeField()
    code_mobile_operators = models.ManyToManyField(CodeMobileOperatorModel, blank=True)
    tags = models.ManyToManyField(TagModel, blank=True)

    def __str__(self) -> str:
        return super().__str__()

    def save(self, *args, **kwargs):
        from .tasks import main_function

        super(MailModel, self).save(*args, **kwargs)

        current_time = timezone.now()
        start_date = self.start_date.replace(tzinfo=utc)
        end_date = self.end_date.replace(tzinfo=utc)
        if start_date <= current_time <= end_date:
            main_function.s(self.id).apply_async(countdown=30)
        elif start_date > current_time and current_time <= end_date:
            main_function.s(self.id).apply_async(eta=self.start_date)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
