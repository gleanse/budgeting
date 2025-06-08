from django.urls import path, include


urlpatterns = [
    path('v1/', include('apps.income.v1.urls')),
]
