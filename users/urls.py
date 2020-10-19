from django.urls import include,path
from rest_framework import routers
from .views import UserViewSet
from .views import EntryPointViewSet


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'entry-points', EntryPointViewSet)

urlpatterns  = [
    path('api/', include(router.urls)),
]
