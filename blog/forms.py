from django import forms
from .models import Post, Comment, Contact


class PostForm(forms.ModelForm):
    """
    Comment form
    """
    class Meta:
        """
        Class that uses bootstrap classes to style fields and
        Populate fields when creating a post.
        """
        model = Post
        fields = ('title', 'author', 'body', 'story_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '', 'id': 'user',
                                             'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        #  Removes the label 'body' from above the comment box
        self.fields['body'].label = "Story"


class CommentForm(forms.ModelForm):
    """
    Form for commenting
    """
    class Meta:
        """
        Class that uses bootstrap classes to style fields and
        Populate fields when commenting on a post.
        """
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
    """
    The contact form for sending comments to site administrator
    """
    class Meta:
        """
        Class that uses bootstrap classes to style fields and
        Populate fields when user uses the contact form.
        """
        model = Contact
        fields = '__all__'
