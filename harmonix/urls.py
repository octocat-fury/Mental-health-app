from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),  # Default route points to login page
    path('home/', views.home, name='home'),  # Home page route
    path('register/', views.register, name='register'),  # Registration page
    path('journal/', views.journal, name='journal'),  # Other routes
    path('archives/', views.archives, name='archives'),
    path('quote/', views.quote_view, name='quote'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path("resources/", views.nami_home, name="resources"),
    path('anxiety_test/', views.submit_test, name='submit_test'),
    path('results', views.results, name='results'),


   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

