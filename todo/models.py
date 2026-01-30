from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200) # The text of the task
    is_done = models.BooleanField(default=False) # Is it checked off?

    def __str__(self):
        return self.title