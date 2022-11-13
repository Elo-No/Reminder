from ..models import Reminder
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

user = {
    'username': 'El@am',
    'phone_number': '09363636366'
}

reminder = {
    'title': 'test model',
    'remind_at': '2022-11-13 7:20:30'
}


@pytest.mark.django_db
def test_create_studium():
    """ 
    Just testing creating objects
    """
    user_instance = User.objects.create(
        **user
    )
    Reminder.objects.create(
        user=user_instance,
        **reminder
    )
    assert Reminder.objects.count() == 1
    print(Reminder.objects.count())
