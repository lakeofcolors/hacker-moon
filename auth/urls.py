from django.urls import include,path
from .views import login,profile
urlpatterns = [
    path('api/login/', login),
    path('api/profile/', profile),
]
