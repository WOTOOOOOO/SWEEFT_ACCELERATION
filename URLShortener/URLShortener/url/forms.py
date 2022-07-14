from django import forms


class Url(forms.Form):
    url = forms.CharField(label="URL")


class CustomUrl(forms.Form):
    url = forms.CharField(label="URL")
    name = forms.CharField(label="NAME")


class Slugs(forms.Form):
    slug = forms.CharField(label="SLUGS")
