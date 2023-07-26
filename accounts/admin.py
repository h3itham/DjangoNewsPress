from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin): 
    add_form = CustomUserCreationForm 
    form = CustomUserChangForm 
    model = CustomUser 
    list_display = ['email', 'username', 'age', 'is_staff', ]
    fieldssets = UserAdmin.fieldsets + (None, {'fields':('age', )})
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields':('age', )}),)

admin.site.register(CustomUser, CustomUserAdmin)