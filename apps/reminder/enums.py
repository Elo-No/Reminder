
from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class RepeatStatus(IntegerChoices):
    DONT_REPEAT = 0, _('Dont Reapeat')
    HOUR_BEFORE = 1, _('Reapeat Hour Before')
    DAY_BEFORE = 2, _('Reapeat Day Before')
    WEEK_BEFORE = 3, _('Reapeat Week Before')
    MONTH_BEFORE = 4, _('Reapea Month Before')


class NotificationStatus(IntegerChoices):
    NONE = 0, _('None')
    FAILED = 1, _('Failed')
    SUCCESS = 2, _('Success')
