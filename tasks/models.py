from django.db import models


class Tasks(models.Model):
    title = models.CharField('title', max_length=100)
    is_completed = models.BooleanField('is_completed', default=False)

    def __str__(self):
        return f'{self.title}'
