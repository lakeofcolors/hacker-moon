from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from users.serializers import UserSerializer
from auth.utils import generate_access_token, generate_refresh_token


@api_view(['GET'])
def profile(request):
    '''
    Get profile info
    '''
    user = request.user
    serialized_user = UserSerializer(user, context={'request':request}).data
    return Response({'user': serialized_user})


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
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

    serialized_user = UserSerializer(user,context={'request':request}).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.data = {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': serialized_user,
    }

    return response
