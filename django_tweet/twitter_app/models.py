from django.db import models

# Create your models here.
class Twit(models.Model):
    nickname = models.CharField(max_length=50) # A field to store the nickname of the user
    content = models.CharField(max_length=280) # A field to store the content of the twit, limited to 280 characters
    def __str__(self):
        return f"{self.nickname}: {self.content}" # Return the content of the twit as a string