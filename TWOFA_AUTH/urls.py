from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('signup/',views.SignupUser,name='signup'),
    path('login/',views.LoginUser,name='login'),
    path('login_with_authenticator/',views.LoginWithAuthenticator,name='loginwithauthenticator'),
    path('exchange_keys/',views.exchange_keys,name='exchangeKeys')    
]

urlpatterns = format_suffix_patterns(urlpatterns)