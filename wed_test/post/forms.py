from django.forms import forms

from .models import Post


class PostForm(forms.Form):

    class Meta():
        model= Post()
        fields = ('title', 'text',)

