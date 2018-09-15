from django import forms


from .models import Post

class PostModelForm(forms.ModelForm):
    content = forms.CharField(label='',
                widget=forms.Textarea(
                        attrs={'placeholder': "Your Post",
                            "class": "form-control"}
                    ))
    class Meta:
        model = Post
        fields = [
            "content"
        ]
