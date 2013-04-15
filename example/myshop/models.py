from django.db import models
from polymorphic.manager import PolymorphicManager
from shop.models.productmodel import Product as ProductShop
from filer.fields.image import FilerImageField
from django.core.urlresolvers import reverse_lazy as reverse

    
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name

class Manufacture(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    logo = FilerImageField(related_name="manufatures")
    logo_front = FilerImageField(related_name="manufactures_logo")
    url = models.CharField(max_length = 500, blank=True, null =True)
    bg_image =FilerImageField(related_name="manufatures_bg")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manufacture_detail", args=[self.slug])        
    @property
    def image(self):
        return self.logo

class Product(ProductShop):
    description = models.TextField()
    category = models.ForeignKey(Category, related_name="products")
    manufacture = models.ForeignKey(Manufacture, related_name='products')
    image = FilerImageField(related_name="products")


    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])
    class Meta:
        pass

class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name="images")
    image = FilerImageField(related_name="images")
