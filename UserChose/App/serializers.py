from rest_framework import serializers

from App.models import User
from App.models import Chose


class ChoseidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chose
        fields = ('id')


class ChoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chose
        fields = ('id', 'size', 'color')