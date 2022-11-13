from celery import shared_task
from django.contrib.auth import get_user_model
from apps.notification.services import sms_handler
from apps.reminder.enums import NotificationStatus

from apps.reminder.models import Reminder
import arrow

User = get_user_model()


@shared_task
def send_sms():
    """
    once each 60(can be modified in .env as SCHEDULE) seconds , will send sms notification
    :return:
    """
    reminders = Reminder.objects.filter(
        notification_status=NotificationStatus.NONE)

    for reminder in reminders:
        data = {
            'user': reminder.user,
            'provider_api': "https://api.ghasedak.me/v2/verification/send/simple",
            'method': "POST",
            'messages': f"Ur appoinment will come at {reminder.remind_at}",
            'line_number': "30005088",
            'send_date': arrow.utcnow(),
            'check_id': None
        }
    appointment_time = arrow.get(reminder.remind_at - reminder.repeat)

    if appointment_time == arrow.utcnow():
        result = sms_handler(data)
        if result['Error']:
            reminder.notification = NotificationStatus.FAILED
        reminder.notification = NotificationStatus.SUCCESS
        reminder.save()
