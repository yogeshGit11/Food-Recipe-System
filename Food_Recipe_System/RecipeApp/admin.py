from django.contrib import admin
from .models import AllRecipes
# Register your models here.

@admin.register(AllRecipes)
class myadmin(admin.ModelAdmin):
    list_display=['id','username','userphone','recipe_title','recipe','timedate']
