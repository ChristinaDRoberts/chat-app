# serializers.py with a serializer for your message model

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from chat.models import Message



# This class is responsible for properly formatting our model as json
# We need to tell it the model to use, and which fields we want included in the json.
class MessageSerializer(ModelSerializer):
    created = serializers.DateTimeField(required=False)
    # user = serializers.
    class Meta:
        model = Message
        fields = ['user', 'text', 'created']
        depth = 1