# -*- coding: utf-8 -*-
from django.contrib import admin
from TestMode1.models import Test,Contact,Tag

# Register your models here.
class ContactAdminSimple(admin.ModelAdmin):
    fields = ('name', 'email')

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email') #list
    search_fields = ('name',)
    inlines = [TagInline] # Inline
    fieldsets = (
        ['main', {
            'fields':('name', 'email'),
        }],
        ['Advance',{
            'classes':('collapse',), #css
            'fields':('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])