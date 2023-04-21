from django.forms import ModelForm, Form
from .models import AccountBook

class LineItemForm(ModelForm):
    class Meta:
        model = AccountBook
        fields = ('date, note, amount)