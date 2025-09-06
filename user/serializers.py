from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False},
        }

    def create(self, validated_data):
        user = CustomUser(
            email = validated_data['email'],
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            role = validated_data.get('role', 'member'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

        # # Token.objects.create(user=user)
        refresh = RefreshToken.for_user(user)
        
        # return {
        #     "user": {
        #         "id": user.id,
        #         "email": user.email,
        #         "username": user.username,
        #         "first_name": user.first_name,
        #         "last_name": user.last_name,
        #         "role": user.role,
        #     },
        #     "access_token": str(refresh.access_token),
        # }

    def to_representation(self, instance):
        # refresh = RefreshToken.for_user(instance)
        # return {
        #     "id": instance.id,
        #     "email": instance.email,
        #     "username": instance.username,
        #     "first_name": instance.first_name,
        #     "last_name": instance.last_name,
        #     "role": instance.role,
        # }
        request = self.context.get('request')
        viewer = request.user if request else None
        data = super().to_representation(instance)

        # Only superuser can see roles
        if not (viewer and viewer.is_superuser):
            data.pop('role', None)
        return data
