#Now that we have customized the user model, we need to create a form to collect the additional information during user registration.
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    gender = forms.ChoiceField(choices=[
        ('M', 'Masculine'),
        ('F', 'Female'),
        ('O', 'Other'),
    ], required=True)
    
    birth_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    phone = forms.CharField(max_length=20, required=True)

    def save(self, request):
        user = super().save(request)
        user.gender = self.cleaned_data.get('gender')
        user.birth_date = self.cleaned_data.get('birth_date')
        user.phone = self.cleaned_data.get('phone')
        user.save()
        return user