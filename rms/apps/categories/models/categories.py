from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'categories'

    def __str__(self):
        return self.name
