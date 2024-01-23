from django.contrib import admin
from . models import *
# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    def truncated_desc(self, obj):
        max_length = 10  # Set the maximum length you desire
        return (obj.description[:max_length] + '...') if len(obj.description) > max_length else obj.description
    list_display = ('name','truncated_desc','email','phone','hired_at','is_mvp')
    list_editable =('is_mvp',)
    list_display_links=('name','phone')
    search_fields=('name','description','email')

admin.site.register(Agent,AgentAdmin)





