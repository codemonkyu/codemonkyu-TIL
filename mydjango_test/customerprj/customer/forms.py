from django import forms


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('name은 3글자 이상 입력해주세요.')


class CustomerFrom(forms.Form):
    name = forms.CharField(validators=[min_length_3_validator])
    text = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    birthdate = forms.DateField()
    Join_date = forms.DateField()
    CHOICES = [('1','남자'),('0','여자'),('2','gay'),('3','transgender')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
