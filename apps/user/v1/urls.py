from django.urls import path
from apps.user.v1.views import UsersView


urlpatterns = [
    path('registration/',UsersView.as_view(), name='user-register'),
]