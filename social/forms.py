from django import forms
from django.contrib.auth.models import User
from social.models import UserProfile





class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # These are the additional fields we want users to have on top of the
        # ones provided by Django's base 'User' model
        fields = ('picture', 'location', 'bio', 'dob', 'university' )

class RegistrationForm(forms.Form):
    
    required_css_class = 'required'
    
   
    username = forms.EmailField(label=("exampleInputEmail1"))
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label=("exampleInputPassword1"))
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label=("exampleInputPassword2"))
    username2 = forms.EmailField(label=("exampleInputEmail2"))
    
    def clean_username(self):
        """
        check it is not already in use.
        
        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['exampleInputEmail1'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['exampleInputEmail1']

    def clean(self):
        """
        check if 2 password match or not
        
        """
        if 'exampleInputPassword1' in self.cleaned_data and 'exampleInputPassword2' in self.cleaned_data:
            if self.cleaned_data['exampleInputPassword1'] != self.cleaned_data['exampleInputPassword2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data

# Don't think we need to add any forms for Universities/subjects/etc as
# this is handled by the Superusers/admins of the site ?
# Also the reason why we only improt UserProfile
