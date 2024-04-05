from rest_framework import serializers
from .models import User, Host
from django.contrib.auth.hashers import make_password


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token

class HostSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(
        read_only=True,
        )
    account_pic = serializers.ImageField(required=False, read_only=False)    
    admins = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, many=True)
    followers = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, many=True)
    notifications = serializers.IntegerField(
        read_only=True,
        )

    class Meta:
        model = Host 
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )


    id = serializers.IntegerField(
        read_only=True,
        )

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)




