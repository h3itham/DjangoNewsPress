
from django import forms 
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm): 
    class Meta(UserCreationForm):
       model = CustomUser 
       fields = ('username', 'email', 'age',)
    #    fields = UserCreationForm.Meta.fields + ('age',)

class CustomUserChangForm(UserChangeForm): 
    class Meta:
        model = CustomUser 
        fields = ('username', 'email', 'age',)

        # fields = UserChangeForm.Meta.fields

