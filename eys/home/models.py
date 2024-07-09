from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import TextInput, EmailInput, Textarea, ModelForm
from django.utils.safestring import mark_safe
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey
import os

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    title = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    description = models.CharField(blank=True,max_length=200)
    company = models.CharField(blank=True,max_length=50)
    address = models.CharField(blank=True,max_length=150)
    phone = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=20)
    smtpserver = models.CharField(blank=True,max_length=20)
    smtppassword = models.CharField(blank=True,max_length=20)
    smtpport = models.CharField(blank=True,max_length=20)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read')
    )
    name = models.CharField(blank=True,max_length=20)
    email = models.EmailField(blank=True,max_length=50)
    subject = models.CharField(blank=True,max_length=50)
    message = models.CharField(blank=True,max_length=200)
    status = models.CharField(max_length=20,choices=STATUS,default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
         return self.name

class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name,surname'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Message'}),

        }

class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )

    categoryname = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE, default=None)
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


    def __str__(self):
        return self.productname

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
