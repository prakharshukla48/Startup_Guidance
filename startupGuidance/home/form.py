from django import forms

#class PredictForm(forms.Form):
#    industry = forms.CharField(label='Your Name', max_length=100)
#    sub_vertical =
#    investment = 

class UniqueForm(forms.Form):
    your_num = forms.CharField(label='Your number')
