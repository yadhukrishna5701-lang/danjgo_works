from rest_framework import serializers
from datetime import datetime
class BookingSerializer(serializers.Serializer):

    team_name = serializers.CharField()

    phone = serializers.CharField()

    email = serializers.EmailField()

    turf = serializers.IntegerField()

    date = serializers.DateField()

    time = serializers.TimeField()

    duration = serializers.CharField()

    created_at = serializers.DateTimeField(read_only = True)

    def validate(self, validated_data):
        date = validated_data.get("date")

        if date < datetime.today().date():
            raise serializers.ValidationError("invalid date")

        return validated_data 
        
    