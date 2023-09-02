from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('signup/',views.SignupUser,name='signup'),
]

urlpatterns = format_suffix_patterns(urlpatterns)