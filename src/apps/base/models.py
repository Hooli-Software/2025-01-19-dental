from django.db import models


class Slide(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title
