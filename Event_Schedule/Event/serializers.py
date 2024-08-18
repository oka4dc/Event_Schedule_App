from .models import Events
from rest_framework import serializers

class EventsSerializer(serializers.ModelSerializer):
    """ serialize Event objects"""
    class Meta:
        model = Events
        fields ="__all__"