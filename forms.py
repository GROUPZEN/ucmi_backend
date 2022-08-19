from tkinter import Widget
from django import forms

class EnquiryForm(forms.Form):
    text = forms.CharField(max_length=45,
    widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Enter todo e.g Grocery Shopping', 'aria-label' : 'Todo', 'aria-describeby' : 'add-btn' }))