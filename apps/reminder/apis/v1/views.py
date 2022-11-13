from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from apps.reminder.apis.v1.serializers import ReminderSerializer

from apps.reminder.models import Reminder


class CreateReminderAPIView(CreateAPIView):
    """
    Create a Reminder
    :param request:
    :return:
    """
    serializer_class =ReminderSerializer
    permission_classes = [IsAuthenticated]

class ListReminderAPIView(ListAPIView):
    """
    Create a Reminder
    :param request:
    :return:
    """
    serializer_class =ReminderSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ('repeat',)
    def get_queryset(self):
        return Reminder.objects.filter(user = self.request.user)

class DetailReminderViewSet(ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # return Reminder.objects.get(
        # user=self.request.user,
        # id=self.kwargs.get('id')).first()
        try:
            return Reminder.objects.get(id=self.kwargs.get('id'))
        except Reminder.DoesNotExist:
            raise Http404

