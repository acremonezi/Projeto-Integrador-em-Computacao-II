from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('create-account/', views.createAccount, name = "Create Account"),
]