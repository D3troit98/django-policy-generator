# Generated by Django 4.0.6 on 2022-07-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_email_address_alter_product_company_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='application_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='website_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='website_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
