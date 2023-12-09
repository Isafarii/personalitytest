# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from traits.views import home, personality_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('traits/', include('traits.urls')),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('personality_test/', personality_test, name='personality_test'),
    # Add other URL patterns as needed
]

# Add the following for serving static files during development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
