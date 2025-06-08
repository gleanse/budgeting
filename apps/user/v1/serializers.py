from rest_framework import serializers
from django.contrib.auth.models import User


class User_Serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','password'] # this field for now ill add fullname someday i think..
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)