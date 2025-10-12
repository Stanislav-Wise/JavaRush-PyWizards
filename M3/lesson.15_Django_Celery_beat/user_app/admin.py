from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_of_birth', 'avatar')
    ordering = ('email',)
    list_filter = ('email',)
    search_fields = ('email', 'username')
    search_help_text = 'Введите часть email или username'
