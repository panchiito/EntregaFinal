
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class MensajeForm(forms.Form):
    asunto = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)

## sector comentarios

TOPIC_CHOICES = (
    ('general', 'Consultas generales'),
    ('bug', 'Comunicar errores'),
    ('suggestion', 'Sugerencias'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)