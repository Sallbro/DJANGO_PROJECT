from django.contrib import admin
from mylpi.models import users

# Register your models here.
# class usersadmin(admin.ModelAdmin):
#     list_display=(user_id,)
admin.site.register(users)
