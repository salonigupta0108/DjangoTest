from django.db import models

class InputString(models.Model):
    input_text = models.CharField(max_length=200)

    def __str__(self):
        return self.input_text

# Create your models here.
