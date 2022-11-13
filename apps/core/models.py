from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """ 
    This is an abstract Django model that can be inherited by other models.
    """

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )

    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Modified at')
    )

    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Is deleted ?'),
    )

    is_archived = models.BooleanField(
        default=False,
        verbose_name=_('Is archived ?'),
    )

    class Meta:
        abstract = True
