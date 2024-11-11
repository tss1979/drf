from rest_framework import serializers

from users.models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'phone']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

