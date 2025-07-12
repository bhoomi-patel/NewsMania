from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border-b-2 border-blue-500 focus:border-blue-700 outline-none w-full py-2 px-1 text-lg',
                'placeholder': 'Enter news title here',
            }),
            'content': forms.Textarea(attrs={
                'class': 'border-b-2 border-blue-500 focus:border-blue-700 outline-none w-full py-2 px-1 text-lg resize-y',
                'placeholder': 'Write the news content here',
                'rows': 6,
            }),
            'category': forms.Select(attrs={
                'class': 'border-b-2 border-blue-500 focus:border-blue-700 outline-none w-full py-2 px-1 text-lg',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full py-2 px-1 text-lg',
                'accept': 'image/*',
                'onchange': 'previewImage(event)',
            }),
        }
