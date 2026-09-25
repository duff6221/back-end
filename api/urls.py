from django.urls import path
from .views import health_check, test_connection

urlpatterns = [
    path("health/", health_check, name="health_check"),
    path("test/", test_connection, name="test_connection"),
]
