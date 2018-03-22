from django import forms
from rpg.models import User, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    academic_score = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    social_score = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    
    class Meta:
        model = UserProfile
        #exclude = ('user',)
        fields = ('picture', 'displayname','academic_score','social_score')#changed

#added euan's part
        
    
