# traits/models.py
from django.db import models


LIKERT_CHOICES = [
    (1, 'Strongly Disagree'),
    (2, 'Disagree'),
    (3, 'Neutral'),
    (4, 'Agree'),
    (5, 'Strongly Agree')#changed to float
]
class PersonalityTestResult(models.Model):
    # Other fields...
    question1_response = models.IntegerField(choices=LIKERT_CHOICES, default=0)
    question2_response = models.IntegerField(choices=LIKERT_CHOICES, default=0)
    question3_response = models.IntegerField(choices=LIKERT_CHOICES, default=0)
    question4_response = models.IntegerField(choices=LIKERT_CHOICES, default=0)
    question5_response = models.IntegerField(choices=LIKERT_CHOICES, default=0)

    # Other fields...

    # Your existing code...


    # ... other fields ...

    case_id = models.IntegerField(default=0)
    country = models.CharField(max_length=255, default='')
    age = models.IntegerField(default=0)
    sex = models.IntegerField(default=0)
    agreeable_score = models.FloatField(default=0.0)
    extraversion_score = models.FloatField(default=0.0)
    openness_score = models.FloatField(default=0.0)
    conscientiousness_score = models.FloatField(default=0.0)
    neuroticism_score = models.FloatField(default=0.0)



class CountryProfile(models.Model):
    country_name = models.CharField(max_length=255)
    average_agreeable_score = models.FloatField(default=0.0)
    average_extraversion_score = models.FloatField(default=0.0)
    average_openness_score = models.FloatField(default=0.0)
    average_conscientiousness_score = models.FloatField(default=0.0)
    average_neuroticism_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"Country Profile: {self.country_name}"
