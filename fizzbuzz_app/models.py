from django.db import models
import uuid

class FizzBuzz(models.Model):
    """
    Represents a FizzBuzz object with an ID, user agent, creation date, and a message.

    Attributes:
        fizzbuzz_id (UUIDField): The unique identifier for the FizzBuzz object.
        useragent (CharField): The user agent of the person who created this FizzBuzz.
        creation_date (DateTimeField): The date and time when the FizzBuzz was created.
        message (TextField): A random message associated with the FizzBuzz.
    """

    fizzbuzz_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    useragent = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
