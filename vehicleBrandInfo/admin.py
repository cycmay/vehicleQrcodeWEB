from django.contrib import admin
from .models import VehicleBrandInfo

# 创建一个ModelAdmin的子类
class AuthorAdmin(admin.ModelAdmin):
    pass

# 注册的时候，将原模型和ModelAdmin耦合起来
admin.site.register(VehicleBrandInfo, AuthorAdmin)
