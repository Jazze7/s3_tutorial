from django  import forms 
from web.models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields="__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

