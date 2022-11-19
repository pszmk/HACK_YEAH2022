from django.db import models

from register.models import Users


# Create your models here.


class CategoryItem(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True, auto_created=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    category_item = models.ForeignKey(CategoryItem, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now=True)
    expiry_date = models.DateField(null=True)
    image = models.ImageField(upload_to="images")
    score = models.IntegerField()
    description = models.CharField(null=True, max_length=300)


    def __str__(self):
        return self.name



