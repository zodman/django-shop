from django.db import models
from polymorphic.manager import PolymorphicManager
from shop.models.productmodel import Product as ProductShop
    
class Category(models.Model):
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

class Manufacture(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Product(ProductShop):
	description = models.TextField()
	category = models.ForeignKey(Category, related_name="products")
	manufacture = models.ForeignKey(Manufacture, related_name='products')
	class Meta:
		pass

class ProductImage(models.Model):
	product = models.ForeignKey(Product)