from django.contrib import admin
from .models import Post, Image, Customer


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Customer)
admin.site.register(Image)
