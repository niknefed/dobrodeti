from django.contrib import admin
from .models import User, Director, Children


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
    list_per_page = 25

admin.site.register(Director)
admin.site.register(Children)