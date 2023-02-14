from django.contrib import admin ,messages
from .models import *

# Register your models here.



class ParticipantFilter (admin.SimpleListFilter):
    title='Participants'
    parameter_name='nbe_participant'
    
    def lookups(self, request, model_admin):
        return (('0' , ('No participants')), 
               ('more',('There are participants')),
                )
    def queryset(self, request, queryset):
        if self.value()=='0':
            return queryset.filter(nbe_participant__exact=0)
        else: 
            return queryset.filter(nbe_participant__gt=0)
        
    
       
class ParticipationInline(admin.StackedInline):
    model=Participation
    extra=1
    classes=['collapse']
    can_delete=True
    readonly_fields=('datePart',)
    
    
    
#pour pouvoir valider les events
def set_state(ModelAdmin, request,queryset):
    rows = queryset.update(state=True)
    if(rows ==1):
        msg="One event was"
    else:
        msg=f"{rows} events were" 
    messages.success(request, message='%s succcessfully accepted '% msg)

set_state.short_description = "Accept"
    
    

class EventAdmin(admin.ModelAdmin):
    def unset_state(self, request,queryset):

        rows_filter=queryset.filter(state=False)
        if rows_filter.count() >0:
            messages.error(request, message=f"{rows_filter.count()} are already refused")
        else:
            rows =  queryset.update(state=False)
            if (rows==1):
                msg="One event was "
            else:
               msg=f"{rows} events were" 
            messages.success(request, message='%s succcessfully refused '% msg)

    unset_state.short_description = "Refuse"
        
    actions=[set_state,"unset_state"]
    actions_on_bottom= True
    actions_on_top= False
    inlines=[
        ParticipationInline
    ]

    list_per_page=20
    
    list_display=(
        'title',
        'Category',
        'state',
    )
    list_filter=(
        'state',
        'Category',
        ParticipantFilter
        
    )
    ordering=('title',)
    #autocomplete_fields=['organizer']
    search_fields=[
        'title',
        'Category',
    ]

    readonly_fields=('created_at',)

    

    fieldsets = (
        (
            'State',
            {
                'fields': ('state',)
            }
        ),
        (
            'About',
            {
                'classes': ('collapse',),
                'fields': (
                    'title',
                    'image',
                    'Category',
                    'organizer',
                    'nbe_participant',
                    'description',
                ),
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    (
                        'evt_date',
                        'created_at',
                    ),
                )
            }
        ),
    )
    
admin.site.register(Event,EventAdmin)
#Autre methode pour enregitrer un model dans l'interface admin est le dècorateur
""" @admin.register(Event) """
