from django.db import models


class SoftwareCategory(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images_software_сategory')

    def __str__(self):
        return f'Category: {self.name}'\
               f'| Description: {self.description}'


class SoftwareSubcategories(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images_software_subcategories')
    category = models.ForeignKey(to=SoftwareCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Subcategories: {self.name}'\
               f'| Description: {self.description}'


class Software(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='images_software')
    subcategories = models.ForeignKey(to=SoftwareSubcategories, on_delete=models.CASCADE)

    def __str__(self):
        return f'Software: {self.name}'\
               f'| Price: {self.price}'\
               f'| Quantity : {self.quantity}'


class FeaturesSoftware(models.Model):
    id_soft = models.ForeignKey(to=Software, on_delete=models.CASCADE)
    description = models.TextField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return f'Id Software: {self.id_soft}'\
               f'| Description: {self.description}'
