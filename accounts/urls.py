from django.urls import path
from accounts.views import signup, user_login

urlpatterns = [
    # tells browser to navigate to recipes and then each recipe
    path('signup/', signup, name='signup'),
    path('login/', user_login, name="user_login")
]
