"""
Serializers for the user API View.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
    )
from django.utils.translation import gettext as _

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serailizer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only' :True, 'min_length': 5}}

    # Post 요청이 오게 되면 실행될 함수
    def create(self,validated_data):
        """Create and return a user with encrypted password."""
        created_user = get_user_model().objects.create_user(**validated_data)
        return created_user
    
    # Update 요청이 오게 되면 실행될 함수
    def update(self, instance, validated_data):
        """Update and return user."""
        password= validated_data.pop('password',None)
        user= super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
    

    
class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token """
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type" : 'password'},
        trim_whitespace =False,
    )

    #특정 계정에 대해 POST 요청이 오면 주게 되는 것은 token 값이다. 
    def validate(self, attrs):
        """Validate and authenticate athe user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password = password,
        )
        if not user:
            msg = _("Unable to authenticate with provided credentials.")
            raise serializers.ValidationError(msg, code = "authorization")
        
        attrs['user'] = user
        return attrs
