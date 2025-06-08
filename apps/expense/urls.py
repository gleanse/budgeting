from django.urls import path, include


urlpatterns = [
    path('v1/', include('apps.expense.v1.urls')),
]