from django.urls import path

from apps.reminder.apis.v1.views import CreateReminderAPIView, DetailReminderViewSet, ListReminderAPIView


app_name = "reminder_v1"

urlpatterns = [
    path("new/", CreateReminderAPIView.as_view(), name="create_reminder_v1"),
    path("", ListReminderAPIView.as_view(), name="list_reminder_v1"),
    path("<int:pk>/detail/", DetailReminderViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    }),name="detail_reminder_v1")

]