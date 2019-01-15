from django.contrib import admin
from .models import Subrediti, Post, Thread, Subscription


class SubreditiAdmin(admin.ModelAdmin):
    """ Tela de admin personalizada para o Subrediti """
    list_display = ['name', 'slug', 'creator']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Subrediti, SubreditiAdmin)
admin.site.register(Post)
admin.site.register(Thread)
admin.site.register(Subscription)
