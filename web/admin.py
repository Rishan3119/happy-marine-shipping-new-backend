from django.contrib import admin
from web.models import RegisterShipForSale

# Register your models here.
class RegShipForSaleAdmin(admin.ModelAdmin):
     list_display=['id','title','vessel_type','short_description','flag','year_built','capacity','LOA','Class','GRT_NRT','Teu','main_engine','DWT','Price','brief_description','email','phone','image']
admin.site.register(RegisterShipForSale,RegShipForSaleAdmin) 
