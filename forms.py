from django import forms
#from polls.models import mymodel

class hform(forms.Form):

	area = forms.CharField(label='Area',max_length=100,required=True)



