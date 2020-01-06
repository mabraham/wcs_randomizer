from django.db import models

class SpotlightDancer(models.Model):
    bib_number = models.IntegerField('Bib Number')
    name = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.name} ({self.bib_number})'
