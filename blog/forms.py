from django import forms
from .models import Post, Comment, Contact


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'title of post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '', 'id': 'user',
                                             'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'value': '', 'id': 'commenter',
                                           'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        #  Removes the label 'body' from above the comment box
        self.fields['body'].label = ""


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
