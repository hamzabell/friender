from.models import User
from django.contrib import admin

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email', 'bio',  'date_of_birth',)
    list_display_links = ('id','email', )
    search_fields = ('first_name', 'last_name', 'email',)
    list_per_page = 10

admin.site.register(User, UserAdmin)