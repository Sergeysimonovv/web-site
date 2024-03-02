from django.db import models

class Price(models.Model):
    title = models.CharField('Наименование', max_length=50)
    price = models.FloatField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'
