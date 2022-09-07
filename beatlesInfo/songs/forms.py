from django import forms

class SongsForm(forms.Form):
  name = forms.CharField(max_length=60)
  composer = forms.CharField(max_length=60)
  album = forms.CharField(max_length=60)
  year = forms.IntegerField()

class InstrumentsForm(forms.Form):
  type = forms.CharField(max_length=40)
  brand = forms.CharField(max_length=40)
  model = forms.CharField(max_length=40)
  year = forms.IntegerField()

