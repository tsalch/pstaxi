from django.db import models

# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length=104, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name_plural = 'Бренды'
        verbose_name = 'Бренд'
