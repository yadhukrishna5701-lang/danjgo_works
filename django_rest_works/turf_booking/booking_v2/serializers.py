from rest_framework import serializers

class TurfBookSerializer(serializers.Serializer):

    id = serializers.CharField(read_only = True)
    name = serializers.CharField()
    location = serializers.CharField()
    phone = serializers.IntegerField()
    fee = serializers.IntegerField()

    def validate(self,validate_data):
        fee = validate_data.get("fee")
        if fee < 250:
            raise serializers.ValidationError("invalid fee and fee <250")
        return validate_data        

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()