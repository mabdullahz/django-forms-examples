from django.db import models

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=50, blank=False)
    review = models.TextField()
    rating = models.IntegerField(blank=False)

    def __str__(self):
        return f'Review from {self.name}, Rating: {self.rating}'
