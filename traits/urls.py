# traits/urls.py
from django.urls import path
from .views import home, personality_test, other_view1, other_view2, test_results, result_page

app_name = 'traits'  # This sets the application namespace

urlpatterns = [
    path('question_list/', other_view1, name='question_list'),
    path('question_template/', other_view2, name='question_template'),
    path('', home, name='home'),
    path('personality_test/', personality_test, name='personality_test'),
    path('test_results/', test_results, name='test_results'),  # Add this line
    path('result_page/', result_page, name='result_page'),  # Add this line for result_page
]
