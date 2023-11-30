from django.urls import path
from core.login.views import *

app_name = 'login'
urlpatterns = [
    path('', LoginFormView.as_view(), name='login_form'),
    path('logout/', LoginRedirectView.as_view(), name='logout'),
]