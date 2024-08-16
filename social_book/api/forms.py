
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control','type': 'password'})
    )
    email = forms.EmailField(
            required=True,
            label='Email',
            widget=forms.EmailInput(attrs={'class': 'form-control','type': 'email'})
        )
    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control','type': 'text' })
    )
    full_name = forms.CharField(
        required=True,
        label='Full Name',
        widget=forms.TextInput(attrs={'class': 'form-control','type': 'text'})
    )
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female')],
        required=True,  
        label='Gender',
        widget=forms.RadioSelect(attrs={'class': 'custom-control-input', 'type': 'radio'})
    )
    city = forms.CharField(
        required=False,
        label='City',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'})
    )
    state = forms.CharField(
        required=False,
        label='State',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'})
    )
    credit_card_type = forms.CharField(
        required=False,
        label='Credit Card Type',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'})
    )
    credit_card_number = forms.CharField(
        required=False,
        label='Credit Card Number',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'})
    )
    cvc = forms.CharField(
        required=False,
        label='CVC',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'})
    )
    expiration_date = forms.DateField(
        required=False,
        label='Expiration Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )


    public_visibility=forms.BooleanField(required=False,
        label='Public Visibility',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input mt-2 ml-2 ', 'type': 'checkbox'  })
    )
    birth_year=forms.IntegerField(
        required=False,
        label='Birth Year',
        widget=forms.NumberInput(attrs={'class': 'form-control ', 'type': 'number'})
    )
    address=forms.CharField(
        required=False,
        label='Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'})
    )

    class Meta:
        model = User
        fields = [
            'username', 'email', 'full_name', 'gender', 'city', 'state',
            'credit_card_type', 'credit_card_number', 'cvc', 'expiration_date',
            'public_visibility', 'birth_year', 'address'
        ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError('Passwords do not match.')
        return cd.get('password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg', 
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg',
        'placeholder': '**********'}))
