from rest_framework import serializers
from django.contrib.auth.models import User
from apps.income.models import Income


class Income_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
