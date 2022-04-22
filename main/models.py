from unicodedata import name
from django.db import models

# Create your models here.
class jobber(models.Model):
    id              = models.IntegerField(primary_key=True)
    name            = models.CharField(max_length=30, default='')
    company_name    = models.CharField(max_length=30, default='')
    #phone = models.PhoneNumberField(_(""))

class store(models.Model):
    id              = models.IntegerField(primary_key=True)
    jobber_id       = models.ForeignKey(jobber, on_delete=models.CASCADE, default='')
    name            = models.CharField(max_length=30, default='')
    nickname        = models.CharField(max_length=10, default='')
    
class uom(models.Model):
    code                = models.CharField(max_length=4, default='')
    name                = models.TextField(max_length=30, default='')
    default_nickname    = models.CharField(max_length=2, unique=True, default='')

class supplier(models.Model):
    id     = models.IntegerField(primary_key=True)
    name   = models.CharField(max_length=30, default='')

    
class store_history(models.Model):
    id                      = models.IntegerField(primary_key=True)
    name                    = models.CharField(max_length=30, default='')
    store_id                = models.ForeignKey(store, on_delete=models.CASCADE, default='')
    jobber_id               = models.IntegerField
    jobber_company_name     = models.CharField(max_length=30, default='')
    product_id              = models.IntegerField
    product_default_uom_code         = models.CharField(max_length=4, default='')
    product_default_uom_nickname     = models.CharField(max_length=4, default='')
    supplier_id             = models.IntegerField
    supplier_name           = models.CharField(max_length=30, default='')
    product_itemnum         = models.CharField(max_length=12, default='')
    product_name            = models.CharField(max_length=30, default='')
    product_description     = models.TextField(max_length=80, default='')
    product_nickname        = models.CharField(max_length=10, unique=True, default='')
    last_order_date         = models.DateField
    
class product(models.Model):
    id      = models.IntegerField(primary_key=True)
    supplier_id     = models.ForeignKey(supplier, on_delete=models.CASCADE, default='') 
    itemnum         = models.CharField(max_length=12, default='')
    name            = models.CharField(max_length=30, default='')   
    description     = models.TextField(max_length=30,default='')
    price           = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    priceunit       = models.CharField(max_length=4, default='')
    pickunit        = models.CharField(max_length=4, default='')
    avgweight       = models.FloatField(default=0)
    
    
class thumanns_product_import(models.Model):
    itemnum         = models.CharField(max_length=12, default='')
    description     = models.TextField(max_length=30,default='')
    price           = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    priceunit       = models.CharField(max_length=4, default='')
    pickunit        = models.CharField(max_length=4, default='')
    avgweight       = models.FloatField(default=0)

