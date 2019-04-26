from django import forms

from .models import com

class comForm(forms.ModelForm):

    class Meta:
        model = com
        fields = ('email', 'comments',)