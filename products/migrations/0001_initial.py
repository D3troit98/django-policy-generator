# Generated by Django 4.0.6 on 2022-07-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150)),
                ('policy_effective_date', models.DateField()),
                ('website_name', models.CharField(max_length=150)),
                ('application_name', models.CharField(max_length=150)),
                ('website_url', models.URLField()),
                ('company_name', models.CharField(max_length=150)),
                ('company_address', models.TimeField()),
                ('country_based', models.CharField(max_length=150)),
            ],
        ),
    ]
