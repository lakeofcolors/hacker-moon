from .models import User
from .models import EntryPoint
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class EntryPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EntryPoint
        fields = '__all__'
