from django.contrib import admin

from mailing.models import Client, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name',)
    search_fields = ('email', 'name')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
