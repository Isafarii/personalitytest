import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()
import csv

# Example to check the latest user in Django shell
from traits.models import PersonalityTestResult
latest_user = PersonalityTestResult.objects.order_by('-id').first()
print(latest_user.agreeable_score, latest_user.extraversion_score, latest_user.openness_score)

def import_personality_data(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8-sig') as csvfile:
        # ... rest of the code
        reader = csv.DictReader(csvfile)
        # Skip the header row
        next(reader, None)
        for row in reader:
            print(row)  # Add this line to inspect the row data

            # Map CSV columns to model fields
            personality_data = {
                'case_id': int(row['case_id']),
                'country': row['country'],
                'age': int(row['age']),
                'sex': int(row['sex']),
                'agreeable_score': float(row['agreeable_score']),
                'extraversion_score': float(row['extraversion_score']),
                'openness_score': float(row['openness_score']),
                'conscientiousness_score': float(row['conscientiousness_score']),
                'neuroticism_score': float(row['neuroticism_score']),
            }


            # Get or create a PersonalityTestResult object
            PersonalityTestResult.objects.get_or_create(
                case_id=personality_data['case_id'],
                defaults=personality_data,
            )

# ...
if __name__ == "__main__":
    # Provide the path to your external CSV file
    csv_file_path = r"C:\Users\Fireb\personality_test\data\big_five_scores1.csv"

    # Call the function to import data
    import_personality_data(csv_file_path)
