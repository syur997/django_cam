from django.forms import ModelForm
from .models import Fileupload

class FileUploadForm(ModelForm):
    class Meta:
        model = Fileupload
        fields = ('__all__')