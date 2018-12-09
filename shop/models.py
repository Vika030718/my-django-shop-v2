from django.db import models

class Category(models.Model):
    name = models.CharField('category title', max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('product title', max_length=200)
    pub_date = models.DateField('date published')
    price = models.IntegerField('product price', default=0)
    image = models.CharField('image url', max_length=255, default='DEFAULT VALUE')
    description = models.CharField('product description', max_length=1000, default='Some description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
