from django.urls import path , include
from .views import *

urlpatterns = [
    path('google_login/', GoogleLogin.as_view(), name='google_login'),
]
