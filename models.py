from django.core.validators import MinValueValidator
from django.contrib.gis.db import models

# Create your models here.

class Event(models.Model):
    title=models.CharField(max_length=255,null=False,blank=False)
    date = models.DateTimeField(auto_now=True, blank=False, null=False)
    location =models.GeometryField(srid=4326, null=True)
    max_attendees=models.IntegerField(validators=[MinValueValidator(1)])


class Attendee(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    email = models.EmailField(max_length=254,unique=True)


class Ticket(models.Model):
    event =models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_tickets')
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='attendee_tickets')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        print('ss')
        if len(self.event.event_tickets.all())== self.event.max_attendees:
            raise ValueError("ظرفیت خالی وجود ندارد")
        return super(Ticket, self).save(force_insert, force_update, using, update_fields)