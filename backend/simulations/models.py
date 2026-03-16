from django.db import models
from django.contrib.auth.models import User
from periodic_table.models import Element

class Material(models.Model):
    name = models.CharField(max_length=100)
    chemical_formula = models.CharField(max_length=100)
    discovered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.chemical_formula})"

class Bond(models.Model):
    BOND_TYPES = (
        ('IONIC', 'Ionic'),
        ('COVALENT', 'Covalent'),
        ('METALLIC', 'Metallic'),
        ('HYDROGEN', 'Hydrogen'),
    )

    material = models.ForeignKey(Material, related_name='bonds', on_delete=models.CASCADE)
    element_1 = models.ForeignKey(Element, related_name='bonds_as_element_1', on_delete=models.CASCADE)
    element_2 = models.ForeignKey(Element, related_name='bonds_as_element_2', on_delete=models.CASCADE)
    bond_type = models.CharField(max_length=20, choices=BOND_TYPES)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.bond_type} bond in {self.material.name}"
