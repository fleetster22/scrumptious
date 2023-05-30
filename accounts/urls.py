from django.urls import path
from accounts.views import signup

urlpatterns = [
    # tells browser to navigate to recipes and then each recipe
    path('signup/', signup, name='signup'),
]
