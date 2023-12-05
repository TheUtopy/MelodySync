from django.contrib import admin

from MelodySync.models.user_model import User
from MelodySync.models.post_model import Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'password')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('message', 'user_id')
