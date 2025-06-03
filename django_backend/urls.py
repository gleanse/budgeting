from django.contrib import admin
from django.urls import path, include
from core.views import home_page

# NOTE: urls of app should be connected here for url endpoint app to project urls

urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]
