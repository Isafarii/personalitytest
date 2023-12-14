# traits/forms.py
from django import forms
from .models import PersonalityTestResult
from traits.models import LIKERT_CHOICES  # Change this line


class PersonalityTestForm(forms.ModelForm):
    question1_response = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    question2_response = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    question3_response = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    question4_response = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    question5_response = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = PersonalityTestResult
        fields = ['question1_response', 'question2_response', 'question3_response','question4_response','question5_response']
