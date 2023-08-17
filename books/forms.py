from django import forms
from .models import Book, Era


# Inspired by Code Institue's "Boutique Ado" Walkthrough Project


class DateInput(forms.DateInput):
    input_type = "date"


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            "published": DateInput(),
            "author": forms.TextInput(
                attrs={'class': 'form-control', 'autocomplete': 'off',
                       'pattern': '[A-Za-z ]+', 'title': 'Enter characters only', 'maxlength': 260}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        eras = Era.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in eras]

        self.fields['era'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
