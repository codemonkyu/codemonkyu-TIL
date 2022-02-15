from django import forms


def min_length_2_validator(value):
    if len(value) < 2:
        raise forms.ValidationError('name은 2글자 이상 입력해주세요.')


class CustomerFrom(forms.Form):
    name = forms.CharField(validators=[min_length_2_validator])
    email = forms.EmailField()
    birthdate = forms.DateField()
    CHOICES = [('1','남자'),('0','여자')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)