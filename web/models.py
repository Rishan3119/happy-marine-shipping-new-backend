from django.db import models

class RegisterShipForSale(models.Model): 
    title = models.CharField(max_length=100,null=True,blank=True)
    vessel_type = models.CharField(max_length=100,null=True,blank=True)
    short_description = models.TextField(null=True,blank=True)
    flag = models.CharField(max_length=100,null=True,blank=True)
    year_built = models.DecimalField(decimal_places=0,max_digits=4)
    capacity = models.CharField(max_length=100,null=True,blank=True)
    LOA = models.CharField(max_length=100,null=True,blank=True)
    Class = models.CharField(max_length=100,null=True,blank=True)
    GRT_NRT = models.CharField(max_length=100, null=True,blank=True)
    Teu = models.CharField(max_length=100,null=True,blank=True)
    main_engine = models.CharField(max_length=100,null=True,blank=True)
    DWT = models.CharField(max_length=100,null=True,blank=True)
    Price = models.CharField(max_length=100,null=True,blank=True)
    brief_description = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.DecimalField(decimal_places=0,max_digits=10,null=True,blank=True)
    image=models.ImageField(upload_to='ship_image',blank=True,null=True)

