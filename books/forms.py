from django import forms
from .models import Book, Era


# Based on Code Institue's "Boutique Ado" Walkthrough Project


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        eras = Era.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in eras]

        self.fields['era'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
