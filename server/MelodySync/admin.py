from django.contrib import admin
from MelodySync.models import User

class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'password')


admin.site.register(User, UserAdmin)
