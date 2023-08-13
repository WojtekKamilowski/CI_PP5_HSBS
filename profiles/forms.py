from django import forms
from .models import UserProfile


# Based on Code Institue's "Boutique Ado" Walkthrough Project


class UserProfileForm(forms.ModelForm):
    # Based on Stackoverflow
    default_phone_number = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[0-9]+', 'title': 'Enter digits only', 'maxlength': 20}))

    # Based on Stackoverflow
    default_town_or_city = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter characters only', 'maxlength': 40}))

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
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }
        # From Teetime
        aria_labels = {
            'default_phone_number': 'Phone number of the user',
            'default_postcode': 'Postal code of the user',
            'default_town_or_city': 'Town or city of the user',
            'default_address1': 'Street address 1 of the user',
            'default_address2': 'Street address 2 of the user',
            'default_county': 'County, state, or locality of the user',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False
