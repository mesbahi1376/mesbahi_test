from rest_framework import routers

from django.urls import path
from .views import *

urlpatterns = [
    path('addEvent', EventViews.as_view({'post': "create"}), name='افزودن رویداد'),
    path('getEvents', EventViews.as_view({'get': "list"}), name='افزودن رویداد'),

    path('addTicket', TicketViews.as_view({'post': "create"}), name='افزودن بلیط'),

]
