from django.contrib import admin
from .models import User
from .models import EntryPoint


admin.site.register(User)
admin.site.register(EntryPoint)
