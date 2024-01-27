from django.contrib import admin
from . models import *
# Register your models here.

class AgentAdmin(admin.ModelAdmin):
   
    list_display = ('name','description','email','phone','hired_at','is_mvp')
    list_editable =('is_mvp',)
    list_display_links=('name','phone')
    search_fields=('name','description','email')

admin.site.register(Agent,AgentAdmin)
admin.site.register(Message)





