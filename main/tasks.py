from config.celery import app
from celery import shared_task
from .models import MailModel, ClientModel, MessageModel
from django.db.models import Q
from .utils import send_msg
from django.utils import timezone
import pytz
from django.core.mail import send_mail
from django.conf import settings
utc = pytz.UTC


@app.task
def main_function(mail_id):
    mail = MailModel.objects.get(id=mail_id)

    clients = ClientModel.objects.filter(
        Q(code_mobile_operator__in=mail.code_mobile_operators.all()) or
        Q(tag__in=mail.tags.all())
    )
    not_sent = []
    for client in clients:
        message = MessageModel(status=MessageModel.Status.WAITING, mail=mail, client=client)
        message.save()
        current_time = timezone.now()
        end_date = mail.end_date.replace(tzinfo=utc)
        if current_time < end_date:
            result = send_msg(message.id, client.phone_number, mail.text)
        else:
            message.status = MessageModel.Status.FAILED
            message.save()
            continue
        if result:
            message.status = MessageModel.Status.SENT
            message.save()
        else:
            not_sent.append(message)

    current_time = timezone.now()
    end_date = mail.end_date.replace(tzinfo=utc)
    if current_time < end_date:
        simple_function.s(not_sent, mail.id).apply_async(countdown=60)


@app.task
def simple_function(message_list, mail_id):
    mail = MailModel.objects.get(id=mail_id)
    end_date = mail.end_date.replace(tzinfo=utc)
    text = mail.text
    current_time = timezone.now()
    not_sent = []
    for message in message_list:
        if current_time < end_date:
            result = send_msg(message.id, message.client.phone_number, text)
        else:
            message.status = MessageModel.Status.FAILED
            message.save()
            continue
        if result:
            message.status = MessageModel.Status.SENT
            message.save()
        else:
            not_sent.append(message)

    current_time = timezone.now()
    if current_time < end_date:
        simple_function.s(not_sent, mail_id).apply_async(countdown=60)


@shared_task(bind=True,
             name='schedule_mail')
def schedule_mail():
    try:
        send_mail(
            'Info',
            'статистику по обработанным рассылкам',
            settings.EMAIL_HOST_USER,
            ['hiha@gmail.com'],
        )
    except Exception as e:
        print(e)

