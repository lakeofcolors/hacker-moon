from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from users.serializers import UserSerializer
from auth.utils import generate_access_token, generate_refresh_token
from users.models import EntryPoint
from .utils import get_client_ip_address
from auth.services.entrypoint import create_entry_point
import logging
import functools
from auth.exceptions.register import RegisterRequiredData
logger = logging.getLogger(__name__)



@api_view(['GET'])
def profile(request) -> Response:
    '''
    Get profile info
    '''
    user = request.user
    serialized_user = UserSerializer(user, context={'request':request}).data
    return Response({'user': serialized_user})

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request) -> Response:
    '''
    Get access and refresh jwt tokens
    '''
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')

    user = User.objects.filter(username=username).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found')
    if (not user.check_password(password)):
        raise exceptions.AuthenticationFailed('wrong password')


    remote_addr = get_client_ip_address(request)
    entry_point_created = create_entry_point(user, remote_addr)

    serialized_user = UserSerializer(user,context={'request':request}).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.data = {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': serialized_user,
    }

    return response

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request) -> Response:


    response = Response()

    User = get_user_model()
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')

    if (username is None) or (password is None) or (email is None):
        raise RegisterRequiredData()


    user = User(
        email=email,
        password=password,
        username=username
    )

    user.save()

    return response
