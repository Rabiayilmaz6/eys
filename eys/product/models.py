from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
import os

class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )

    categoryname = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE, default=None)
    slug = models.SlugField(default='')

    class MPTTMeta:
        order_insertion_by = ['categoryname']

    def __str__(self):
        return self.categoryname

class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    productname = models.CharField(max_length=100, default='')
    description = RichTextUploadingField()
    url = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    stock = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE, default=None)

    class MPTTMeta:
        order_insertion_by = ['productname']

    def __str__(self):
        full_path = [self.productname]
        k = self.parent
        while k is not None:
            full_path.append(k.productname)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    def image_tag(self):
        if self.url:
            image_path = os.path.join(settings.MEDIA_ROOT, self.url.name)
            if os.path.exists(image_path):
                return mark_safe('<img src="{}" width="50" height="50" />'.format(self.url.url))
            else:
                return "Image file does not exist"
        return "No Image"

    image_tag.short_description = 'Image'

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    imagename = models.CharField(max_length=50, blank=True, default='')
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.imagename

    def image_tag(self):
        if self.image:
            image_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            if os.path.exists(image_path):
                return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
            else:
                return "Image file does not exist"
        return "No Image"
