from django.urls import path
from .views import FizzBuzzListCreate, FizzBuzzRetrieve

urlpatterns = [
    path('fizzbuzz/', FizzBuzzListCreate.as_view(), name='fizzbuzz-list-create'),
    path('fizzbuzz/<uuid:fizzbuzz_id>/', FizzBuzzRetrieve.as_view(), name='fizzbuzz-retrieve'),
]
