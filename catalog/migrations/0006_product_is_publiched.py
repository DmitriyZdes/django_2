# Generated by Django 5.0 on 2024-04-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_publiched',
            field=models.BooleanField(default=False, verbose_name='признак публикации'),
        ),
    ]