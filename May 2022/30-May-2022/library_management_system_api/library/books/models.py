from django.db import models

# Create your models here.
class Book(models.Model):
    isbn= models.CharField(max_length=50)
    title= models.CharField(max_length=200)
    genre= models.CharField(max_length=50)
    publisher= models.CharField(max_length=100)
    language= models.CharField(max_length=10)
    no_of_pages = models.IntegerField (blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

