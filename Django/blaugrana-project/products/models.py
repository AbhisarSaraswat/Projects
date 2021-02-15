from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Product(models.Model):

    title = models.CharField(max_length=250)
    description = models.TextField()
    # image = models.ImageField(upload_to='images/')
    type = models.CharField(max_length=250)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title


def get_image_filename(instance, filename):
    title = instance.product.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')
