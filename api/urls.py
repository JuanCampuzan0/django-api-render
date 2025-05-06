from django.urls import path
from .views import authors

urlpatterns = [
    path('authors', authors),
]
