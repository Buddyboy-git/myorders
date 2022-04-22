from django import forms
from django.contrib import admin
from .models import jobber, store, store_history, uom, product, supplier, thumanns_product_import
from django.utils.html import mark_safe

# Register your models here.
#admin.site.register(store)
#admin.site.register(store_history)
admin.site.register(jobber)
admin.site.register(product)
admin.site.register(supplier)


# Create admin model displays here.

class JobberChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.company_name)

class StoreChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.name)

     
class storeAdmin(admin.ModelAdmin):

    list_display= ('name', 'get_jobber', 'nickname')
    @admin.display(description='Jobber Name', ordering='jobber__company_name')

    def get_jobber(self, obj):
        return obj.jobber_id.company_name


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'jobber_id':
            return JobberChoiceField(queryset=jobber.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(store, storeAdmin)

class tpiAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('admin/css/mycustom.css',)
        }


    def asCurrency(self, obj): # Here
        return mark_safe("$%s" % (obj.price))


    list_display= ('itemnum','description','asCurrency','priceunit','pickunit','avgweight')
    search_fields = ('itemnum','description','price')
admin.site.register(thumanns_product_import,tpiAdmin)

class storeHistoryAdmin(admin.ModelAdmin):
    def get_jobber(self, obj):
        return obj.jobber_id.company_name

    def get_store(self, obj):
        return obj.store_id.name

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'jobber_id':
            return JobberChoiceField(queryset=jobber.objects.all())
        if db_field.name == 'name':
            return StoreChoiceField(queryset=store.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    list_display=('pk', 'store_id', 'name', 'product_itemnum', 'product_default_uom_code', 'product_nickname', 'product_name', 'product_description', 'jobber_company_name')
admin.site.register(store_history,storeHistoryAdmin)

class uomAdmin(admin.ModelAdmin):
    list_display=('code', 'name', 'default_nickname')
admin.site.register(uom, uomAdmin)
