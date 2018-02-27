from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse 
from .models import VehicleBrandInfo
from .forms import VehicleBrandInfoForm

#import pillow
import qrcode
import time
import os

QRURL_ENDPOINT = 'http://95.163.203.111:8080/'
# Create your views here.
#表单展示
def info(request, info_pk):
    info = get_object_or_404(VehicleBrandInfo, pk=info_pk)

    context = {
        'info':info,
    }
    return render(request, 'vehicleBrandInfo/vehicleBrandInfo.html', context=context) 

#表单填写完毕跳转
def form2QRcode(request):
    if request.method == 'POST':
        form = VehicleBrandInfoForm(request.POST)
        form.save()

        context = {
            'form':form,
        }
        all_pk = len(VehicleBrandInfo.objects.all())
        info = VehicleBrandInfo.objects.filter(pk=all_pk)
        code_url = QRURL_ENDPOINT + '/vehicleBrandInfo/info/' + str(all_pk)

        qr=qrcode.QRCode(version=3, box_size=5, border=0)
        qr.add_data(code_url)
        img = qr.make_image()  
        img_name = str(int(time.time()*1000))+'.png'
        dest = os.path.join(settings.STATIC_ROOT, 'media/', img_name) 
        img.save(dest)
        img_dest = 'media/' + img_name
        return render(request, 'vehicleBrandInfo/QRcodeshow.html', context={'img_name':img_dest, 'code_url':code_url})

#表单界面
def form_to_fill(request):
    form = VehicleBrandInfoForm()
    context = {
        'form': form,
    }
    return render(request, 'vehicleBrandInfo/vehicleBrandForm.html', context=context)
