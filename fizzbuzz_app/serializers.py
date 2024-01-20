from rest_framework import serializers
from .models import FizzBuzz

class FizzBuzzSerializer(serializers.ModelSerializer):
    """
    Serializer for the FizzBuzz model.

    Converts FizzBuzz instances to JSON format and vice-versa, validating data in the process.
    """

    useragent = serializers.CharField(required=False) # read-only
    class Meta:
        model = FizzBuzz
        fields = ['fizzbuzz_id', 'useragent', 'creation_date', 'message']
