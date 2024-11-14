from django.db import models
from cats.models import Cat

class Mission(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission for {self.cat.name} - {'Completed' if self.complete else 'In Progress'}"
