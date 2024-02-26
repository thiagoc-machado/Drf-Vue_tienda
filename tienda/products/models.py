from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Categoría', related_name='get_products')
    description = models.CharField(max_length= 255, verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name