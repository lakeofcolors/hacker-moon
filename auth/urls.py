from django.urls import include,path
from .views import login,profile,register


urlpatterns = [
    path('api/login/', login),
    path('api/register/',register),
    path('api/profile/', profile),
]
