from rest_framework import serializers
from .models import Pairs


class PairSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pairs
        fields = ('id', 'roman', 'arabic')
