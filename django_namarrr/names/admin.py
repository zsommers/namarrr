from django.contrib import admin
from names.models import Adjective, Noun, Surname


class WordAdmin(admin.ModelAdmin):
    """Create custom admin page for words"""
    fieldsets = [
        (None,          {'fields': ['text']}),
        ('Vote Totals', {'fields': ['upvotes', 'downvotes'],
                         'classes': ['collapse']})
    ]
    list_display = ('text', 'weight')
    search_fields = ['text']

# Register your models here.
admin.site.register(Adjective, WordAdmin)
admin.site.register(Noun, WordAdmin)
admin.site.register(Surname, WordAdmin)
