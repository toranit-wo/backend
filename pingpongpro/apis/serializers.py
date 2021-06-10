from rest_framework import serializers
from pingponghit.models import Pingponghit


class PingponghitSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title',
            'data',
            'total'
        )
        model = Pingponghit


