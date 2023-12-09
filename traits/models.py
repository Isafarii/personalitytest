from django.db import models

class PersonalityTestResult(models.Model):
    question1_response = models.IntegerField(default=3)
    question2_response = models.IntegerField(default=3)
    question3_response = models.IntegerField(default=3)
    # ... other fields



    # Add more fields for other questions

    def __str__(self):
        return f"Personality Test Result {self.id}"
