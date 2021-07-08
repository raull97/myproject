from django.urls import path
from .views import login_view, logout_view, signup, homepage

urlpatterns = [
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('signup', signup),
    path('', homepage),
]