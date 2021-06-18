from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from healing_chakra_app.models import SignUpCredentials, LoginCredentials, MedicineDonation, EquipmentDonation


class SignUpCredentialsAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'name', 'email', 'mobile', 'aadhaar', 'location']


class MedicineDonationAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'mobile', 'aadhaar', 'location', 'medicine_name', 'manufacture_date',
                    'expiry_date']


class EquipmentDonationAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'mobile', 'aadhaar', 'location', 'equipment_name', 'manufacture_date']

class LoginCredentialsAdmin(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(SignUpCredentials, SignUpCredentialsAdmin)
admin.site.register(MedicineDonation, MedicineDonationAdmin)
admin.site.register(EquipmentDonation, EquipmentDonationAdmin)
admin.site.register(LoginCredentials, LoginCredentialsAdmin)
