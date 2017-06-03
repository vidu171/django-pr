from django.contrib import admin
from .models import Users
from .models import Token

admin.site.Register(Users)
admin.site.Register(Token)
# Register your models here.
