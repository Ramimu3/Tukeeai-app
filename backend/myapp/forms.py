from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput(attrs={'id': 'file_input'}))

    class Meta:
        model = UploadedFile
        fields = ['file']
