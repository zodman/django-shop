from django.db import models
from polymorphic.manager import PolymorphicManager
from shop.models.productmodel import Product as ProductShop
from filer.fields.image import FilerImageField
    
class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField()
	
	def __unicode__(self):
		return self.name

class Manufacture(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField()
	logo = FilerImageField(related_name="manufatures")
	logo_front = FilerImageField(related_name="manufactures")
        url = models.CharField(max_length = 500, blank=True, null =True)

	def __unicode__(self):
		return self.name

class Product(ProductShop):
	description = models.TextField()
	category = models.ForeignKey(Category, related_name="products")
	manufacture = models.ForeignKey(Manufacture, related_name='products')
        image = FilerImageField(related_name="products")

	class Meta:
		pass

class ProductImage(models.Model):
	product = models.ForeignKey(Product)
        image = FilerImageField(related_name="productimages")
