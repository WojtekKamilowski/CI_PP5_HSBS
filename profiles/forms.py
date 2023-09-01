from django import forms
from .models import UserProfile


# Based on Code Institue's "Boutique Ado" Walkthrough Project


class UserProfileForm(forms.ModelForm):
    # Based on Stackoverflow
    default_phone_number = forms.CharField(required=False,
                                           widget=forms.TextInput(
                                               attrs={
                                                   'class': 'form-control',
                                                   'autocomplete': 'off',
                                                   'pattern': '[0-9]+',
                                                   'title': 'Digits only',
                                                   'maxlength': 20
                                               }))

    # Based on Stackoverflow
    default_town_or_city = forms.CharField(required=False,
                                           widget=forms.TextInput(
                                               attrs={
                                                   'class': 'form-control',
                                                   'autocomplete': 'off',
                                                   'pattern': '[A-Za-z ]+',
                                                   'title': 'Letters only',
                                                   'maxlength': 40
                                               }))

    # Based on Stackoverflow
    default_county = forms.CharField(required=False,
                                     widget=forms.TextInput(
                                         attrs={
                                             'class': 'form-control',
                                             'autocomplete': 'off',
                                             'pattern': '[A-Za-z ]+',
                                             'title': 'Letters only',
                                             'maxlength': 80
                                         }))

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders & classes, removes auto-generated
        labels and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_address1': 'Street Address (house, street)',
            'default_address2': 'Street Address (additional info)',
            'default_county': 'County, State or Locality',
        }
        # Based on Teetime
        aria_labels = {
            'default_phone_number': 'Delivery phone number of the user',
            'default_postcode': 'Delivery postal code of the user',
            'default_town_or_city': 'Delivery town or city of the user',
            'default_address1': 'Delivery street address 1 of the user',
            'default_address2': 'Delivery street address 2 of the user',
            'default_county': 'Delivery county, or locality of the user',
            'default_country': 'Delivery country of the user',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            else:
                self.fields[field].label = False
                self.fields[field].widget.attrs['aria-label'] = aria_labels[
                    field
                ]
