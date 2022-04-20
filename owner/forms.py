from django import forms
from django.forms import ModelForm
from owner.models import Books
from customer.models import Orders

class BookForm(ModelForm):
    class Meta:
        model=Books
        fields='__all__'
        widgets={
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'copies': forms.TextInput(attrs={'class': 'form-control'}),
            'published_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            # 'image':forms.FileInput(attrs={'class':'form-control'})


        }



    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get('price')
        copies=cleaned_data.get('copies')


        if int(price)<0:
            msg="invalid entry"
            self.add_error('price',msg)

        if int(copies)<0:
            msg="invalid entry"
            self.add_error("copies",msg)


class OrderProcessForm(ModelForm):
    options = (
        ('dispatched', 'dispatched'),
        ('intransit', 'intransit'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled')

    )
    status=forms.ChoiceField(choices=options)
    class Meta:
        model=Orders
        fields=['delivery_address','phone','status','expected_delivery_date']
        widgets={

            "delivery_address":forms.Textarea(attrs={"class":"form-control","readonly":True}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "status":forms.Select(attrs={"class":"form-control"}),
            "expected_delivery_date":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }


