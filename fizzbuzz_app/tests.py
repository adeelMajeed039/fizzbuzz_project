from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import FizzBuzz

import factory

class FizzBuzzFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FizzBuzz

    message = factory.Faker('sentence')


class FizzBuzzTests(APITestCase):
    def test_create_fizzbuzz(self):
        """
        Ensure we can create a new FizzBuzz object.
        """
        url = reverse('fizzbuzz-list-create')
        data = {'message': 'Hello, world!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FizzBuzz.objects.count(), 1)
        self.assertEqual(FizzBuzz.objects.get().message, 'Hello, world!')
    
    def test_list_fizzbuzz(self):
        """
        Ensure we can list all FizzBuzz objects.
        """
        FizzBuzz.objects.create(message='Test 1')
        FizzBuzz.objects.create(message='Test 2')

        url = reverse('fizzbuzz-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_fizzbuzz(self):
        """
        Ensure we can retrieve a FizzBuzz object.
        """
        fizzbuzz = FizzBuzz.objects.create(message='Test retrieve')
        url = reverse('fizzbuzz-retrieve', kwargs={'fizzbuzz_id': fizzbuzz.fizzbuzz_id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Test retrieve')
    
    def test_list_fizzbuzz_with_factory(self):
        """
        Ensure we can list all FizzBuzz objects created by factory.
        """
        FizzBuzzFactory.create_batch(3)  # Create 3 FizzBuzz objects

        url = reverse('fizzbuzz-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
    
    def test_retrieve_fizzbuzz_with_factory(self):
        """
        Ensure we can retrieve a FizzBuzz object created by factory.
        """
        fizzbuzz = FizzBuzzFactory()  # Create a FizzBuzz object

        url = reverse('fizzbuzz-retrieve', kwargs={'fizzbuzz_id': fizzbuzz.fizzbuzz_id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], fizzbuzz.message)
    
    def test_create_fizzbuzz_invalid_data(self):
        """
        Ensure that creating a FizzBuzz object with invalid data fails.
        """
        url = reverse('fizzbuzz-list-create')
        data = {}  # Missing 'message' field
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
