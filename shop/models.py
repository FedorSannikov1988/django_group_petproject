from django.db import models

class SoftwareCategory(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images_software_сategory')

    def __str__(self):
        return f'Категория: {self.name} '\
               f'| Описание категории: {self.description}'

class SoftwareSubcategories(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images_software_subcategories')
    category = models.ForeignKey(to=SoftwareCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Подкатегория: {self.name} '\
               f'| Описание подкатегории: {self.description} '\
               f'| Категория к которой она относиться: {self.category}'

class Software(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    number_licenses = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='images_software')
    subcategories = models.ForeignKey(to=SoftwareSubcategories, on_delete=models.CASCADE)

    def __str__(self):
        return f'Название софта: {self.name} '\
               f'| Описание: {self.description} '\
               f'| Цена 1-ой лицензии: {self.price} '\
               f'| Количество лицензий: {self.number_licenses} '\
               f'| Подкатегория к которой относиться софт: {self.subcategories}'