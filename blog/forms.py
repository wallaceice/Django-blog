from django import forms
from .models import *

choices  = Category.objects.all().values_list('name','name')

category_list = []
for category_item in choices:
    category_list.append(category_item)
    
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'category', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'placeholder exemple'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = category_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'placeholder exemple'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }