from django.db import models 


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category
    class Meta:
        ordering=['category']
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=50,verbose_name="Product Name")
    description = models.TextField(default="",null=False, verbose_name="Description Of Product")
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.PositiveSmallIntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='photos/%y/%m/%d') #year month day
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name
