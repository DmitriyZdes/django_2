from django.db import models
from users.models import User


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(max_length=100, verbose_name='описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='превью')
    price = models.IntegerField(verbose_name='цена')
    created_date = models.DateTimeField(verbose_name="дата создания")
    change_date = models.DateTimeField(verbose_name="дата последнего изменения")
    is_publiched = models.BooleanField(default=False, verbose_name='признак публикации')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='владелец', null=True, blank=True)

    def __str__(self):

        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('can_deny_publish_product', 'Can cancel publishing'),
            ('can_edit_desription', 'Able to change description'),
            ('can_edit_category', 'Can change category')
        ]


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=100, verbose_name="описание")

    def __str__(self):

        return f'{self.name} {self.description}'

    class Meta:

        verbose_name = "категория"
        verbose_name_plural = "категории"


class Version(models.Model):

    ver_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    ver_number = models.IntegerField(verbose_name='номер версии')
    ver_name = models.CharField(max_length=150, verbose_name='название версии')
    is_current_vers = models.BooleanField(default=True)

    def __str__(self):

        return self.ver_name

    class Meta:

        verbose_name = 'версия'
        verbose_name_plural = 'версии'
