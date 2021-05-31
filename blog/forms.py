from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','header_image','header_image2','header_image3','tags']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})

            
        }
