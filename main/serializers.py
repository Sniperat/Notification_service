from rest_framework import serializers
from .models import ClientModel, MailModel, MessageModel


class MessageModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageModel
        fields = '__all__'


class ClientModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientModel
        fields = '__all__'


class MailModelSerializer(serializers.ModelSerializer):

    total_sent = serializers.ReadOnlyField()
    total_failed = serializers.ReadOnlyField()
    total_retry = serializers.ReadOnlyField()

    class Meta:
        model = MailModel
        fields = '__all__'


