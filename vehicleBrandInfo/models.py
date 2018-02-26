from django.db import models

# Create your models here.
class VehicleBrandInfo(models.Model):
    """docstring for VehicleBrandInfo"""  
    license_plate = models.CharField(max_length=20) #车牌号
    driver_name = models.CharField(max_length=20)   #驾驶员姓名
    start_place = models.CharField(max_length=30)   #起始地
    end_place = models.CharField(max_length=30)     #终到地
    sign_serial_number = models.CharField(max_length=20)    #标志牌顺序号
    transport_company = models.CharField(max_length=40)     #运输企业
    business_issuer = models.CharField(max_length=20) #企业签发人
    main_apporach = models.CharField(max_length=40) #主要途径地
    effective_date = models.CharField(max_length=40) #有效期


