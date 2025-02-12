from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for view user details.
    """
    class Meta:
        model = User
        fields ='__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration with all required fields.
    """
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, min_length=8, required=True)
    full_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'full_name', 'phone_number', 'address']
        

    def create(self, validated_data):
        """
         Create and return a new user with the validated data.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data.get('full_name'),
            phone_number=validated_data.get('phone_number'),
            address=validated_data.get('address')
        )
        return user


# Serializer to handle user details update
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
    def update(self, instance, validated_data):
        """
         update and return instance data of users.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
