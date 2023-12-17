from django.contrib import admin
from django.contrib.auth.admin import UserAdmin#odatda superuserlarga etgishli class
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'age','manzili','is_staff']#bu qatorni kiritmaydigan bolsak django oz standarti boyicha admin panelda
    #users malumotlarini korsataveradi ammo biz unga ham ozimiz istagan narsalarni chiqaradigan qilib ozgartirsak boladi
    fieldsets = UserAdmin.fieldsets +(
        (None,{'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields': ('age',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)# bu qatorsiz admin panelda mqlumot korinmaydi
