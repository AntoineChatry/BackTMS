from rest_framework import serializers
from .models import TMS

class TmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TMS
        fields = ('id', 'classroom', 'building', 'completed', 'seats', 'rows','columns')