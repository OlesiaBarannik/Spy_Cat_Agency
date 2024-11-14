from django.db import models

class Cat(models.Model):
    BREED_CHOICES = [
        ('siamese', 'Siamese'),
        ('persian', 'Persian'),
        ('maine_coon', 'Maine Coon'),
        ('british_shorthair', 'British Shorthair'),
    ]

    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=50, choices=BREED_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name