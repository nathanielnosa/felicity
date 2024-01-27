from django.contrib import admin
from . models import *
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    def truncated_title(self, obj):
        max_length = 10  # Set the maximum length you desire
        return (obj.title[:max_length] + '...') if len(obj.title) > max_length else obj.title

    list_display = ('listing_id','truncated_title','price','status','listing_type','created_at','agent','is_published')
    list_display_links=('listing_id','truncated_title')
    list_filter =('agent',)
    list_editable=('is_published',)
    search_fields = ('price','title','description','address')
    list_per_page = 3


class CategoryAdmin(admin.ModelAdmin):
     search_fields = ('category',)

admin.site.register(Listing,ListingAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Inquiry)
