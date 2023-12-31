from django import forms
from .models import Order


# Based on Code Institue's "Boutique Ado" Walkthrough Project


class OrderForm(forms.ModelForm):
    # From Stackoverflow
    full_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'pattern': '[A-Za-z ]+',
            'title': 'Enter letters only',
            'maxlength': 50
        }))

    # Based on Stackoverflow
    phone_number = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'pattern': '[0-9]+',
            'title': 'Enter digits only',
            'maxlength': 20
        }))

    # Based on Stackoverflow
    town_or_city = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'pattern': '[A-Za-z ]+',
            'title': 'Enter letters only',
            'maxlength': 40
        }))

    # Based on Stackoverflow
    county = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'pattern': '[A-Za-z ]+',
            'title': 'Enter letters only',
            'maxlength': 80
        }))

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address (house number, street name)',
            'street_address2': 'Street Address (additional info)',
            'county': 'County, State or Locality',
        }
        # Based on Teetime
        aria_labels = {
            'full_name': 'Full Name of the customer',
            'email': 'Email Address of the customer',
            'phone_number': 'Phone Number of the customer',
            'postcode': 'Postal Code of the customer',
            'town_or_city': 'Town or City of the customer',
            'street_address1': 'Street Address (house number, street name)',
            'street_address2': 'Street Address (additional info) for delivery',
            'county': 'County, State or Locality of the customer',
            'country': 'Country of the customer',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['aria-label'] = aria_labels[
                field
            ]
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
