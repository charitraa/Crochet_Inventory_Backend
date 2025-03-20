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
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({'email': 'A user with this email already exists.'})
        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({'username': 'A user with this username already exists.'})
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data.get('full_name'),
            phone_number=validated_data.get('phone_number'),
            address=validated_data.get('address')
        )
        return user

class AdminAddUserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration with all required fields.
    """
    email = serializers.EmailField(required=True)
    full_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    role = serializers.ChoiceField(choices=[('admin', 'Admin'), ('general', 'General')], write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'phone_number', 'address', 'role']

    def create(self, validated_data):

        """
        Create and return a new user with the validated data.
        If role is 'admin', set is_staff to True.
        """
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({'email': 'A user with this email already exists.'})

        role = validated_data.pop('role')  # Extract role before creating user

        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data.get('full_name'),
            phone_number=validated_data.get('phone_number'),
            address=validated_data.get('address'),
            profile_pic=validated_data.get('profile_pic')
        )

        if role == 'admin':
            user.is_staff = True
            user.save()

        return user


# Serializer to handle user details update
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'full_name', 'phone_number', 'address']
        
    def update(self, instance, validated_data):
        """
         update and return instance data of users.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
