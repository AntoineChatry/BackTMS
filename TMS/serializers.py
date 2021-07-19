from rest_framework import serializers
from .models import TMS

class TmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TMS
        fields = ('id', 'title', 'description', 'completed', 'places')