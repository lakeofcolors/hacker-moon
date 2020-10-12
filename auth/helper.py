import jwt
import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model


class JWTAuthentication(BaseAuthentication):
    '''
    Link: https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
    '''
    def authenticate(self, request):

        User = get_user_model()
        authentication_header = request.headers.get('Authorization')

        if not authentication_header:
            return None

        try:
            access_token = authentication_header.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algoritms=['HS256'])
          
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Access token expired')

        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        user = User.objects.filter(id=payload["user_id"]).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        return (user,None)
