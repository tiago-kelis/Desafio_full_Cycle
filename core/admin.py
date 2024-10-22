from django.contrib import admin
from .models import Post, Tag

# Use a classe padrão AdminSite para registro dos modelos
admin.site.register(Post)
admin.site.register(Tag)
