from django import forms
from rpg.models import User, UserProfile

#User sign-up form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#User statistics form
class UserProfileForm(forms.ModelForm):
    academic_score = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    social_score = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

    no_grads = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    no_viper = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    no_homework = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    no_tennent = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    no_drop = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

    class Meta:
        model = UserProfile
        fields = ('picture', 'displayname','academic_score','social_score'
        ,'no_grads','no_viper','no_homework','no_tennent','no_drop')




