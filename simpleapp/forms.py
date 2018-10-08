from django import forms
from django.core.validators import MaxValueValidator


class LaptopCreateForm(forms.Form):
     name       = forms.CharField(max_length=120)
     quantity   = forms.IntegerField(validators=[MaxValueValidator(500),])

     def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass