from rest_framework import serializers

from Test.models import Event, Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('created_at','attendee',)
        depth = 1

class AddTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):

    event_tickets = TicketSerializer(many=True,read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {'event_tickets': {'read_only': True}}





