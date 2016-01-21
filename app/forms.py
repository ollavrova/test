from django.core.validators import URLValidator
from django.forms import forms, URLField


class UrlInputForm(forms.Form):
    url = URLField(validators=[URLValidator()])
