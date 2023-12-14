# traits/urls.py

from django.urls import path
from .views import home, personality_test, test_results, result_page, other_view1, other_view2, compare_results

app_name = 'traits'

urlpatterns = [
    path('', home, name='home'),
    path('personality_test/', personality_test, name='personality_test'),
    path('result_page/', result_page, name='result_page'),
    path('compare_results/', compare_results, name='compare_results'),  # Check this line
    path('other_view1/', other_view1, name='other_view1'),
    path('other_view2/', other_view2, name='other_view2'),
]
