from rest_framework import serializers
from powers.models import SuperHeros

class SuperHerosSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    powers = serializers.CharField()
    category = serializers.CharField()
    weakness = serializers.CharField()
    universe = serializers.CharField()
    