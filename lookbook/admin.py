from django.contrib import admin

from .models import Collection, Slide_of_collection

class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name")

admin.site.register(Collection)


admin.site.register(Slide_of_collection)

