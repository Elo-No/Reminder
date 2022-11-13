from rest_framework.serializers import ModelSerializer, ValidationError
from timezone_field import TimeZoneField
from django.core.exceptions import ValidationError
import arrow

from apps.reminder.models import Reminder


class ReminderSerializer(ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'user', 'title','description','remind_at','repeat')
        read_only =('id',)

    def validate(self, attrs):
        appointment_time = arrow.get(attrs['remind_at'])

        if appointment_time < arrow.utcnow():
            raise ValidationError(
                'You cannot schedule an appointment for the past. '
                )
        return attrs