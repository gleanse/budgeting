from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Expense, Income, Money


class User_Serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','password'] # this field for now ill add fullname someday i think..
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class Expense_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class Income_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class Money_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = '__all__'