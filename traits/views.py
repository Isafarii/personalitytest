# traits/views.py
from django.shortcuts import render, redirect
from .models import PersonalityTestResult
from .forms import PersonalityTestForm


def home(request):
    return render(request, 'traits/home.html')

def personality_test(request):
    if request.method == 'POST':
        form = PersonalityTestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the results to the database
            return redirect('traits:test_results')  # Redirect to a results page with the correct namespace
    else:
        form = PersonalityTestForm()

    return render(request, 'traits/personality_test.html', {'form': form})

def test_results(request):
    # Get the answers from the latest PersonalityTestResult (assuming it's the last one saved)
    latest_result = PersonalityTestResult.objects.last()
    
    # Assuming there are three questions (question1_response, question2_response, question3_response)
    answers = [latest_result.question1_response, latest_result.question2_response, latest_result.question3_response]

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
    # Add logic to fetch results from the database or any other processing
    results = {'result1': 'Some result for question 1', 'result2': 'Some result for question 2', 'result3': 'Some result for question 3'}

    return render(request, 'traits/result_page.html', {'results': results})

def other_view1(request):
    # Your implementation for other_view1
    pass

def other_view2(request):
    # Your view logic here
    return HttpResponse("Hello, this is other_view2!")
