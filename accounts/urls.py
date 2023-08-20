from django.contrib import admin
from django.urls import path
from django.urls import path
from accounts.views import CSRFToken, RegisterView


urlpatterns = [
    path("register/",RegisterView.as_view(),name="accounts"),
    path("csrf/",CSRFToken.as_view(),name="csrf"),
]



