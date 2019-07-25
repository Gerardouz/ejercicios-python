from django.contrib import admin

# Register your models here.


from .models import User, Auto


admin.site.register(User)
admin.site.register(Auto)