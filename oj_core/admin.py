from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Problem)
admin.site.register(Data)
admin.site.register(UserStatus)
admin.site.register(Status)