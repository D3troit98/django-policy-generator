# Generated by Django 4.0.6 on 2022-07-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_application_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='password',
            field=models.TextField(default='123456'),
        ),
    ]
