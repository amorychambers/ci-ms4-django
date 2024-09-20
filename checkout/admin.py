from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total')

    fields = ('order_number', 'date', 'full_name', 'email',
              'phone_number', 'street_address1', 'street_address2',
              'town_or_city', 'county', 'postcode',
              'collection', 'order_total')
    
    list_display = ('order_number', 'date', 'full_name',
                    'collection', 'order_total')
    
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)