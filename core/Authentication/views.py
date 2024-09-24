# accounts/views.py

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.authtoken.models import Token

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

    def get_response(self):
        response = super().get_response()
        token , created = Token.objects.get_or_create(user=user)
        response.data['token'] = str(token)  # اضافه کردن توکن به پاسخ
        return response
