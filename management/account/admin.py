from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Manager


class ManagerAdmin(UserAdmin):
    '''
     Custom Admin for Manager
    '''
    model = Manager
    list_display = ('email','is_staff','is_active','firstname','lastname','company')
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
   
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'firstname','lastname','date_of_birth','is_staff', 'is_active')}
        ),
    )
    ordering = ('email',)
admin.site.register(Manager,ManagerAdmin)