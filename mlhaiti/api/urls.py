from django.urls import path, include

from mlhaiti.accounts.api import views as  account_views

urlpatterns = [
    # ACCOUNT END-POINTS
    path('accounts/register', account_views.UserCreateView.as_view(), name='register'),
    path('accounts/login', account_views.UserLoginView.as_view(), name='login'),
]
