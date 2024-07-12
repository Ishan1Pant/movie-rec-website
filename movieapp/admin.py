from django.contrib import admin
from .models import newsletter,contact
# Register your models here.
admin.site.site_header='Movie Recommendation System'
admin.site.site_title='Movie Rec'
admin.site.index_title='Manage Movie Rec'

class fieldadmin(admin.ModelAdmin):
    list_display=('name','email','msg')
    search_fields=('msg',)

admin.site.register(newsletter)
admin.site.register(contact,fieldadmin)