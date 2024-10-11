from django.contrib import admin
from web.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(Post,PostAdmin)