from django.urls import path

from .views import authorization_views

urlpatterns = [
    path('login/', authorization_views.AuthorizationView.as_view(), name='login'),
]