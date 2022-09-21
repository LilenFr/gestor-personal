from django.forms import ModelForm
from .models import Contact

class ContacForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)

