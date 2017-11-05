from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

GENDER_CHOICES= [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
    ]

LOC_CHOICES= [
    ('Clark', 'Clark'),
    ('Alderman', 'Alderman'),
    ('Thornton Stacks', 'Thornton Stacks')
    ]

NUM_CHOICES= [
    ('> 2', '> 2'),
    ('any size', 'any size')
    ]

MALE_CHOICES= [
    ('only men', 'only men'),
    ('anyone', 'anyone')
    ]

FEMALE_CHOICES= [
    ('only women', 'only women'),
    ('anyone', 'anyone')
    ]

OTHER_CHOICES= [
    ('only men', 'only men'),
    ('only women', 'only women'),
    ('anyone', 'anyone')
    ]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    firstname = forms.CharField(label='First name', max_length=254)
    gender = forms.CharField(label='Gender:', widget=forms.Select(choices=GENDER_CHOICES))
    password1 = forms.CharField(label='Password', max_length=254, widget=forms.PasswordInput,
                                help_text='Your password can\'t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can\'t be a commonly used password. Your password can\'t be entirely numeric.')

    class Meta:
        model = User
        fields = ('username', 'firstname', 'email', 'password1', 'password2', 'gender')

class ReadyForm(forms.ModelForm):
    dep_location = forms.CharField(label='Departure location', widget=forms.Select(choices=LOC_CHOICES), initial='Thornton Stacks')
    num_companions = forms.CharField(label='Desired number of companions', widget=forms.Select(choices=NUM_CHOICES), initial='any size')
    destination = forms.CharField(label='Departure location', widget=forms.Select(choices=LOC_CHOICES), initial='Clark')

    class Meta:
        model = User
        fields = ('dep_location', 'num_companions', 'destination')

class MaleForm(forms.ModelForm):
    companions = forms.CharField(label='Companions', widget=forms.Select(choices=MALE_CHOICES), initial='anyone')

    class Meta:
        model = User
        fields = ('companions',)

class FemaleForm(forms.ModelForm):
    companions = forms.CharField(label='Companions', widget=forms.Select(choices=FEMALE_CHOICES), initial='anyone')

    class Meta:
        model = User
        fields = ('companions',)

class OtherForm(forms.ModelForm):
    companions = forms.CharField(label='Companions', widget=forms.Select(choices=OTHER_CHOICES), initial='anyone')

    class Meta:
        model = User
        fields = ('companions',)
