# Generated by Django 5.0 on 2024-02-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_confirmationcode_user_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_code',
            field=models.CharField(default=0, max_length=100, verbose_name='код верификации'),
        ),
    ]