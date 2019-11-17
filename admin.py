from django.contrib import admin

# Register your models here.
from .models import bestiary,terrain_details,terrain_items,buildings,events

admin.site.register(bestiary)
admin.site.register(terrain_details)
admin.site.register(terrain_items)
admin.site.register(buildings)
admin.site.register(events)

