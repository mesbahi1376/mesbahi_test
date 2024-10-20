from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Test.models import Event, Ticket
from Test.serializers import EventSerializer, AddTicketSerializer


# Create your views here.

class EventViews(ModelViewSet):
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'list':
            return EventSerializer


class TicketViews(ModelViewSet):
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return AddTicketSerializer