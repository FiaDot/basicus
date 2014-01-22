from django.db import models


class Categories(models.Model):
    Title = models.CharField(maxlength=40, null=False)


class Article(models.Model):
    Title = models.CharField(max_length=80)
    Body = models.TextField(null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey(Categories)
    Comments = models.PositiveIntegerField(default=0, null=True) 


class Comments(models.Model):
    Name = models.CharField(max_length=20, null=False)
    Password = models.CharField(max_length=32, null=False)
    Content = models.TextField(max_length=2000, null=False)
    Created = models.DateTimeField(auto_now_add=True, auto_now=True)