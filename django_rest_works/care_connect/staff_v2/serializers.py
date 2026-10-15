from rest_framework import serializers
from staff.models import Doctor
class DoctorSerializer(serializers.Serializer):

    id = serializers.CharField(read_only = True)
    name = serializers.CharField()
    specialization = serializers.ChoiceField(choices=Doctor.SPECIALIZATION_OPTIONS)
    fee = serializers.IntegerField()
    qualification = serializers.CharField()
    email = serializers.EmailField()

    def validate(self,validate_data):
        fee = validate_data.get("fee")
        if fee < 250:
            raise serializers.ValidationError("invalid fee and fee <250")
        return validate_data        

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()