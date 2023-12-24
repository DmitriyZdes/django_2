from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=50, verbose_name='заголовок')
    slug = models.CharField(max_length=50, verbose_name='разборчивый url')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='media/blog', verbose_name='превью', null=True, blank=True)
    creation_date = models.DateField(verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    count_view = models.PositiveIntegerField(verbose_name='количество просмотров')

    def __str__(self):

        return self.title


    class Meta:

        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
