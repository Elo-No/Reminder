from django.urls import reverse, resolve

import pytest
from apis.v1 import views


@pytest.mark.parametrize("url, target_class", [
    ("reminder_v1:create_reminder_v1", views.CreateReminderAPIView)
])
def test_correct_url_binding(url, target_class):
    """ 
    Just testing revers url is correct or not (for create reminder api)
    """
    url = reverse(url)
    assert resolve(url).func.view_class == target_class


@pytest.mark.parametrize("url, target_class", [
    ("reminder_v1:list_reminder_v1", views.ListReminderAPIView)
])
def test_correct_url_binding(url, target_class):
    """ 
    Just testing revers url is correct or not (for list reminder api)
    """
    url = reverse(url)
    assert resolve(url).func.view_class == target_class
