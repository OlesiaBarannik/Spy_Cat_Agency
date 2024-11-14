from django.db import models
from missions.models import Mission


class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='targets')
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    complete = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.complete or self.mission.complete:
            if hasattr(self, '_original_notes') and self.notes != self._original_notes:
                raise ValueError("Cannot update notes if mission or target is completed.")
            else:
                self._original_notes = self.notes

        super(Target, self).save(*args, **kwargs)