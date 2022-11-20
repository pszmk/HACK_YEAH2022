from django.db import models

# Create your models here.


class CategoryItem(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True, auto_created=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    category_item = models.ForeignKey(CategoryItem, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text


