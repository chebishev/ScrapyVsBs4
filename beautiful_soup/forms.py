from django import forms


class SearchForm(forms.Form):
    site = forms.URLField(label="", widget=forms.URLInput(
        attrs={'placeholder': 'https://example.com', 'class': 'form-control'}))
