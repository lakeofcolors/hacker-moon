from .models import User
from .models import EntryPoint
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from .serializers import EntryPointSerializer
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class EntryPointViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that entry point to be viewed or edited
    '''
    queryset = EntryPoint.objects.all().order_by('-timestamp')
    serializer_class = EntryPointSerializer
