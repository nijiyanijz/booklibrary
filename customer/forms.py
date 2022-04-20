from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from customer.models import Orders,Reviews

class UserRegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'})),
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})

        }

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['delivery_address','phone']
        widgets={
            'delivery_address':forms.Textarea(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'})
        }
class ReviewForm(forms.ModelForm):
    class Meta:
        models=Reviews
        fields=["review","rating"]
        widgets={
            "review":forms.Textarea(attrs={'class':'form-control'}),

        }
        options=(
            ('1','1'),
            ('1.5','1.5'),
            ('2', '2'),
            ('2.5', '2.5'),
            ('3', '3'),
            ('3.5', '3.5'),
            ('4', '4'),
            ('4.5', '4.5'),
            ('5','5')

        )
        rating=forms.ChoiceField(choices=options)
