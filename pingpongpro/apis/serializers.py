from rest_framework import serializers
from pingponghit.models import Pingponghit,Totalhit


class PingponghitSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title',
            'data',
        )
        model = Pingponghit

class TotalhitSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title',
            'total'
        )
        model = Totalhit

