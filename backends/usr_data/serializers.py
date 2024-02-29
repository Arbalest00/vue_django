from rest_framework import serializers
from .models import usr_data

class usr_data_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usr_data
        fields = "__all__"
        