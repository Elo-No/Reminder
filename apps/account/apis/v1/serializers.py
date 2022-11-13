from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from utils.validatoin_phone import phone_number_validation

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(
        write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation',
                  'phone_number', 'first_name', 'last_name')

    def validate(self, attrs):
        if not phone_number_validation(attrs['phone_number']):
            raise serializers.ValidationError(
                {"phone_number": "phone number is not valid"})
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )

        # user.set_password(validated_data['password'])
        # user.save()

        return user
