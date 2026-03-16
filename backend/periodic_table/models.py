from django.db import models

class Element(models.Model):
    name = models.CharField(max_length=100, unique=True)
    symbol = models.CharField(max_length=5, unique=True)
    atomic_number = models.IntegerField(unique=True)
    atomic_mass = models.FloatField()
    group = models.IntegerField(null=True, blank=True)
    period = models.IntegerField()
    category = models.CharField(max_length=100) # e.g. "Noble Gas", "Alkali Metal"
    electron_configuration = models.CharField(max_length=100, blank=True)
    electronegativity = models.FloatField(null=True, blank=True)
    atomic_radius = models.FloatField(null=True, blank=True) # Empirically measured in pm (or we can just store whatever the json gives)
    density = models.FloatField(null=True, blank=True)
    melt = models.FloatField(null=True, blank=True) # Melting point in K
    boil = models.FloatField(null=True, blank=True) # Boiling point in K
    phase = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['atomic_number']

    def __str__(self):
        return f"{self.name} ({self.symbol})"
