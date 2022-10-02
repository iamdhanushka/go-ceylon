from django.contrib import admin
from .models import *


#admin.site.register(Destination)
admin.site.register(Review)
admin.site.register(Admin)
admin.site.register(OCRImage)


class DestionationImageAdmin(admin.StackedInline):
    model=DestinationImage

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    inlines=[DestionationImageAdmin]

    class Meta:
        model = Destination

@admin.register(DestinationImage)
class DestinationImageAdmin(admin.ModelAdmin):
    pass



