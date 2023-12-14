# traits/views.py
from django.shortcuts import render, redirect
from .models import PersonalityTestResult, CountryProfile
from .forms import PersonalityTestForm
from django.db.models import Avg

# traits/views.py

# traits/views.py

def personality_test(request):
    if request.method == 'POST':
        form = PersonalityTestForm(request.POST)
        if form.is_valid():
            # Save the results to the database
            user_result = form.save(commit=False)

            # Print form data for debugging
            print("Form Data:", form.cleaned_data)

            # Calculate and set scores based on user responses
            user_result.agreeable_score = calculate_score(form.cleaned_data['question1_response'])
            user_result.extraversion_score = calculate_score(form.cleaned_data['question2_response'])
            user_result.openness_score = calculate_score(form.cleaned_data['question3_response'])

            # Calculate and set conscientiousness and neuroticism scores
            user_result.conscientiousness_score = calculate_score(form.cleaned_data['question4_response'])
            user_result.neuroticism_score = calculate_score(form.cleaned_data['question5_response'])

            user_result.save()

            return redirect('traits:result_page')  # Redirect to the results page

    else:
        form = PersonalityTestForm()

    return render(request, 'traits/personality_test.html', {'form': form})

# traits/views.py

def calculate_score(response):
    # Debugging print statements
    print("Response:", response)

    try:
        response = int(response)  # Convert the response to an integer
    except ValueError:
        print("Invalid Response: Not an integer")
        return 0.0  # Set a default value for invalid responses

    # Check if the response is in the Likert scale
    if 1 <= response <= 5:
        print("Mapped Score:", response)
        return float(response)  # Convert to float if needed
    else:
        print("Invalid Response: Out of range")
        return 0.0  # Set a default value for out-of-range responses

def home(request):
    return render(request, 'traits/home.html')

# traits/views.py

def compare_results(request):
    # Fetch the latest user from the CSV data
    latest_user = PersonalityTestResult.objects.order_by('-id').first()

    # Calculate user scores based on individual question responses
    user_scores = {
        'agreeable_score': latest_user.agreeable_score,
        'extraversion_score': latest_user.extraversion_score,
        'openness_score': latest_user.openness_score,
        'conscientiousness_score': latest_user.conscientiousness_score,
        'neuroticism_score': latest_user.neuroticism_score,
    }

    # Query database to get similar users based on CSV data
    similar_users = PersonalityTestResult.objects.filter(
        country=latest_user.country,
    ).exclude(id=latest_user.id)[:20]  # Fetch top 20 similar users from the same country

    average_scores = {
        'agreeable_score': similar_users.aggregate(Avg('agreeable_score'))['agreeable_score__avg'] or 0.0,
        'extraversion_score': similar_users.aggregate(Avg('extraversion_score'))['extraversion_score__avg'] or 0.0,
        'openness_score': similar_users.aggregate(Avg('openness_score'))['openness_score__avg'] or 0.0,
        'conscientiousness_score': similar_users.aggregate(Avg('conscientiousness_score'))['conscientiousness_score__avg'] or 0.0,
        'neuroticism_score': similar_users.aggregate(Avg('neuroticism_score'))['neuroticism_score__avg'] or 0.0,
    }

    # Pass data to the template for rendering
    context = {
        'user_data': latest_user,
        'user_scores': user_scores,
        'similar_users': similar_users,
        'average_scores': average_scores,
    }

    return render(request, 'traits/compare_results.html', context)

def calculate_similarity(user_scores, average_scores, country_profile):
    # Calculate Euclidean distance between user scores and average scores
    similarity_score = sum((user_scores[key] - average_scores[key])**2 for key in user_scores) ** 0.5

    # You can further refine the similarity calculation based on your specific requirements
    # For example, you might want to give more weight to certain traits or use a different formula

    return similarity_score



def test_results(request):
    # Get the answers from the latest PersonalityTestResult
    latest_result = PersonalityTestResult.objects.last()

    # Assuming there are three questions (question1_response, question2_response, question3_response)
    answers = [
        int(latest_result.question1_response),
        int(latest_result.question2_response),
        int(latest_result.question3_response),
    ]

    # Your logic based on Likert scale responses
    # For example, you can calculate an average or apply your specific logic
    average_response = sum(answers) / len(answers)

    # Customize the result based on the average response
    if average_response >= 4:
        result = 'You have a high score!'
    elif average_response >= 2:
        result = 'You have a moderate score.'
    else:
        result = 'You have a low score.'

    # Render the result_page.html template with the calculated result
    return render(request, 'traits/result_page.html', {'result': result})


def result_page(request):
    # Fetch the latest user from the CSV data
    latest_user = PersonalityTestResult.objects.order_by('-id').first()

    # Pass the latest user's scores to the template for rendering
    context = {
        'latest_user_scores': {
            'agreeable_score': latest_user.agreeable_score,
            'extraversion_score': latest_user.extraversion_score,
            'openness_score': latest_user.openness_score,
            'conscientiousness_score': latest_user.conscientiousness_score,
            'neuroticism_score': latest_user.neuroticism_score,
        },
    }

    return render(request, 'traits/result_page.html', context)
def other_view1(request):
    # Your implementation for other_view1
    pass

def other_view2(request):
    # Your view logic here
    return HttpResponse("Hello, this is other_view2!")

