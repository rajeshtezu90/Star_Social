from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm # subclass of forms.ModelForm

class UserCreateForm(UserCreationForm):
    
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()  # Returns the User model that is  currently active in this project.
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"