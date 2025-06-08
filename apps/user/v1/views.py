
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.user.v1.serializers import User_Serializer


class UsersView(APIView):
    def post(self, request):
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)