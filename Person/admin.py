from django.contrib import admin
from .models import *

# Register your models here.


def set_state(ModelAdmin, request,queryset):
    rows = queryset.update(is_active=True)
    if(rows ==1):
        msg="One user was"
    else:
        msg=f"{rows} users were" 
    messages.success(request, message='%s succcessfully accepted '% msg)

set_state.short_description = "Accept"

class UserAdmin(admin.ModelAdmin):
    def unset_state(self, request,queryset):
        rows_filter=queryset.filter(is_active=False)
        if rows_filter.count() >0:
            messages.error(request, message=f"{rows_filter.count()} are already refused")
        else:
            rows =  queryset.update(is_active=False)
            if (rows==1):
                msg="One event was "
            else:
               msg=f"{rows} events were" 
            messages.success(request, message='%s succcessfully refused '% msg)
               

    unset_state.short_description = "Refuse"
    actions=[set_state,"unset_state"]
    actions_on_bottom= True
    actions_on_top= False

    list_per_page=20
 
    list_display=(
        'username',
        'first_name',
        'last_name',
        'cin',
        'email',
        'is_active'
    )
    list_filter=(
        'first_name',
        'last_name',
        
        
    )
    ordering=('username',)

    search_fields=[
        'cin',
        'username',
    ]

    #readonly_fields=('createdAt',)
    
    
    fieldsets = (
        (
            'State',
            {
                'fields': ('is_active',)
            }
        ),
        (
            'Personal Information',
            {
                'classes': ('collapse',),
                'fields': ('username','first_name','last_name','email','cin')
            }
        ),
        (
            'Password',
            {
                'classes': ('collapse',),
                'fields': (
                    'password',
                ),
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    (
                        'last_login',
                        'date_joined',
                    ),
                )
            }
        ),
    )

admin.site.register(Person,UserAdmin)

