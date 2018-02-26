from django import forms
from .models import VehicleBrandInfo


class VehicleBrandInfoForm(forms.ModelForm):
    class Meta:
        model = VehicleBrandInfo
        fields = ['license_plate', 'driver_name', 'start_place', 'end_place', 'sign_serial_number', 
                    'transport_company', 'business_issuer', 'main_apporach', 'effective_date', 
                    ]