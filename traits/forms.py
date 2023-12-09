# traits/forms.py
from django import forms
from .models import PersonalityTestResult

class PersonalityTestForm(forms.ModelForm):
    class Meta:
        model = PersonalityTestResult
        fields = ['question1_response', 'question2_response', 'question3_response']  # Update fields here
