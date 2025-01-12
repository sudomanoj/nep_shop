from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from auth_profile.models import User
from django.forms import ModelForm

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
        
        
class UserForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ("__all__")
        
    
        
class UserCustomCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields ="__all__"
