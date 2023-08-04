from django.contrib import admin
from . models import User, Asset

# Register your models here.
admin.site.register(User)

class AssetAdmin(admin.ModelAdmin):
    list_display = 'name','type','purchased_at','updated_at','deleted_at','status'
    
admin.site.register(Asset)
