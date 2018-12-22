from django.contrib import admin
from .models import Todo
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    """Django admin ModelAdmin for data model NAME"""
    model = Todo
    list_display = ('title_name', 'pub_date')
    ordering = ('pub_date',)
    search_fields = ('title_name',)

admin.site.register(Todo,TodoAdmin)
