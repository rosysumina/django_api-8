from rest_framework.serializers import ModelSerializer
from apis.accounts.models import User

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        field = '__all__'


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        field = ('email', 'first name', 'last name', 'password')


    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
