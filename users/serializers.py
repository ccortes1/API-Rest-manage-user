""" User serializers """

# Django
from django.conf import settings
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator


# Django Rest Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Models
from users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializer. """
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "date_birth",
            "mobile_phone",
            "email",
            "address",
            "session_active",
            "password",
        )

    def create(self, data):
        """Handle user creation."""
        user = User.objects.create_user(**data )
        return user

class UserLoginSerializer(serializers.Serializer):
    """ User login serializer
    Handle the login request data.
    """
    mobile_phone = serializers.CharField(max_length=17)
    password = serializers.CharField(min_length=4, max_length=64)

    def validate(self, data):
        """ Check credentials """
        #print(data['password'])
        user = authenticate(username=data['mobile_phone'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """ Generate or retrive new token. """
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
