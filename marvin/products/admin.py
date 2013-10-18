from django.conf import settings
from django.contrib import admin

from .models import Grape, Country, Appellation, Wine, Winemaker


class GrapeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['common_name']}),
        ('Detailed Info', {
            'fields': ['latin_name'],
            'classes': ['collapse']
            })
    ]


admin.site.register(Grape, GrapeAdmin)
admin.site.register(Country)
admin.site.register(Appellation)
admin.site.register(Wine)
admin.site.register(Winemaker)
