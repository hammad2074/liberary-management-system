from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUseradmin 
from .models import User

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ('email','full_name','is_staff','is_active')
    search_fields = ('full_name','email')
    list_filter = ('is_staff','is_active')
    ordering = ('email',)



