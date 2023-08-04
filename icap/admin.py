from django.contrib import admin
from . models import User, Asset

admin.site.site_header = "ICAP Dashboard"
admin.site.index_title = "Welcome to the ICAP Dashboard"

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'created_at')

class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'type', 'purchased_at', 'updated_at', 'deleted_at', 'status')
    list_filter = ('user', 'purchased_at', 'updated_at', 'deleted_at', 'status')
    search_fields = ('name', 'type', 'purchased_at', 'updated_at', 'user__name')
    
admin.site.register(User, UserAdmin)
admin.site.register(Asset, AssetAdmin)
