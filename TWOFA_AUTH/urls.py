from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('signup/',views.SignupUser,name='signup'),
    path('login/',views.LoginUser,name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)