from rest_framework import generics
from .models import FizzBuzz
from .serializers import FizzBuzzSerializer
from rest_framework.permissions import AllowAny

class FizzBuzzListCreate(generics.ListCreateAPIView):

    """
    API view to list and create FizzBuzz objects.

    GET requests return a list of all FizzBuzz objects.
    POST requests create a new FizzBuzz object with the provided message.
    """

    queryset = FizzBuzz.objects.all()
    serializer_class = FizzBuzzSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        useragent = self.request.META.get('HTTP_USER_AGENT', '')
        serializer.save(useragent=useragent)

class FizzBuzzRetrieve(generics.RetrieveAPIView):

    """
    API view to retrieve a specific FizzBuzz object.

    GET requests return the FizzBuzz object with the provided fizzbuzz_id.
    """
    
    queryset = FizzBuzz.objects.all()
    serializer_class = FizzBuzzSerializer
    permission_classes = [AllowAny]
    lookup_field = 'fizzbuzz_id'
