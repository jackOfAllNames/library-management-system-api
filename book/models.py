from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"
