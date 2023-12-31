from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(max_length=100, verbose_name='описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='превью')
    price = models.IntegerField(verbose_name='цена')
    created_date = models.DateTimeField(verbose_name="дата создания")
    change_date = models.DateTimeField(verbose_name="дата последнего изменения")

    def __str__(self):

        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=100, verbose_name="описание")



    def __str__(self):

        return f'{self.name} {self.description}'

    class Meta:

        verbose_name = "категория"
        verbose_name_plural = "категории"
