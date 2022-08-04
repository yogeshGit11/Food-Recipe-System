from django.db import models

# Create your models here.

class AllRecipes(models.Model):
    username=models.CharField(max_length=100)
    userphone=models.CharField(max_length=10)
    recipe_title=models.CharField(max_length=100)
    recipe=models.CharField(max_length=10000)
    timedate=models.DateTimeField(auto_now=True,blank=True)
