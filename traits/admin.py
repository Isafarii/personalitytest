# traits/admin.py
from django.contrib import admin
from .models import PersonalityTestResult, CountryProfile

admin.site.register(PersonalityTestResult)
admin.site.register(CountryProfile)
