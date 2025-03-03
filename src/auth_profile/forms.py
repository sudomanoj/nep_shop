from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from auth_profile.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms

class UserAddForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAddForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        
        if commit:
            user.save()
        return user      
class UserUpdateForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = "__all__"
    
        
class UserCustomCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields ="__all__"


class CustomAdminAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Email or Phone Number",
        widget=forms.TextInput(attrs={"autofocus": True}),
    )
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            # Check if input is a phone number or email
            if "@" in username:
                user = authenticate(email=username, password=password)
            else:
                user = authenticate(phone_number=username, password=password)

            if user is None:
                raise forms.ValidationError("Invalid email/phone number or password.")

            self.user_cache = user

        return self.cleaned_data
