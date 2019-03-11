from django.contrib import admin

# Register your models here.
from App.models import User, Chose


admin.site.register(User)
admin.site.register(Chose)