from django.contrib import admin
from django.urls import path, include
from . import views

# NOTE: urls of app should be connected here for url endpoint app to project urls

urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.income.urls')),
]
