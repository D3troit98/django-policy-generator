from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    header = models.CharField(max_length=150 , null=False)
    policy_effective_date= models.DateField(null=False)
    website_name = models.CharField(max_length=150,null=True)
    application_name = models.CharField(max_length=150, null=True)
    website_url = models.URLField(blank=True,null=True)
    company_name = models.CharField(max_length=150, null=False)
    company_address = models.TextField(null=False)
    country_based = models.CharField(max_length=150,null=False)
    email_address  = models.EmailField(default='anonymouse@gmail.com',null=False)
    password = models.TextField(default='123456',null=False )


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    header = models.CharField(max_length=200 , null=False)
    website_name = models.CharField(max_length=150,null=True)
    application_name = models.CharField(max_length=150, null=True)
    website_url = models.CharField(max_length=250 , null=False)
    company_name = models.CharField(max_length=150, null=False)
    company_address = models.TextField(null=False)
    country_based = models.CharField(max_length=150,null=False)
    email_address  = models.EmailField(default='anonymouse@gmail.com',null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email_address + "\n" + self.company_name

class Input(models.Model):
    input = models.IntegerField()