
from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _

class GenderStatus(IntegerChoices):
    NONE = 0 , _('None')
    MALE = 1 , _('Male')
    FAMALE = 2 , _('Female')


