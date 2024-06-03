"""URLs for accounts app."""
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # Login page
    path('login/', views.login, name='login'),
    # Registration page.
    path('register/', views.register, name='register'),
    # Successful registration
    path('register/successful-registration/',
         views.successful_registration, name='successful_registration'),
    # User profile
    path('profile/', views.profile, name='profile'),
    # Physical information page.
    path('profile/physical-information/', views.physical_information, name='physical-information'),
]
