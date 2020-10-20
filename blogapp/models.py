from django.db import models
from imagekit.models import ImageSpecField # < import this
from imagekit.processors import ResizeToFill # < import this
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe 
import os

# Create your models here.
class Logo(models.Model):
    Title       = models.CharField(max_length=50)
    Image       = models.ImageField(upload_to="logo/",blank= True)
    icon        = models.ImageField(upload_to="logo/",blank= True)
    Status      = models.BooleanField(default = True)
    header_image = models.ImageField(upload_to="logo/",blank= True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos' 

class category(models.Model):
    Title       = models.CharField(max_length=50)
    Status      = models.BooleanField(default = True)

    def __str__(self):
        return self.Title
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'category' 


class slider(models.Model):
    image       = models.ImageField(upload_to="slider/",blank= True)
    Title       = models.CharField(max_length=150)
    Status      = models.BooleanField(default = True)

    def __str__(self):
        return self.Title
    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'slider' 

class service(models.Model):
    Title       = models.CharField(max_length=150)
    icon        = models.CharField(max_length=150,blank= True)
    discription = models.TextField(max_length=550,blank= True)
    Status      = models.BooleanField(default = True)

    def __str__(self):
        return self.Title
    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'


class about_us(models.Model):
    Title       = models.CharField(max_length=150)
    about_us    = RichTextField()
    image       = models.ImageField(upload_to="slider/",blank= True)
    Status      = models.BooleanField(default = True)

    def __str__(self):
        return self.Title
    class Meta:
        verbose_name = 'about_us'
        verbose_name_plural = 'about_us' 


class store_location(models.Model):
    Title       = models.CharField(max_length=150)
    store_map   = models.TextField(blank=True)
    Status      = models.BooleanField(default = True)

    def __str__(self):
        return self.Title
    class Meta:
        verbose_name = 'store_location'
        verbose_name_plural = 'store_locations' 


class user_message(models.Model):
    name       = models.CharField(max_length=150)
    email      = models.CharField(max_length=150,blank=True)
    message    = models.TextField(blank=True)
    date       = models.DateTimeField( auto_now=True, auto_now_add=False)
    Status     = models.BooleanField(default = True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'user_message'
        verbose_name_plural = 'user_messages' 


class product(models.Model):
    category   = models.ForeignKey(category, on_delete=models.CASCADE)
    name       = models.CharField(max_length=250)
    image1     = models.ImageField(upload_to="product/",blank=True)
    image2     = models.ImageField(upload_to="product/",blank=True)
    image3     = models.ImageField(upload_to="product/",blank=True)
    power      = models.CharField(max_length=50,blank=True)
    company    = models.CharField(max_length=150,blank=True)
    indication = models.TextField(blank=True)
    dosage     = models.TextField(blank=True)
    side_efect = models.TextField(blank=True)
    therapeutic_class  = models.TextField(blank=True)
    pack_price  = models.CharField(max_length=50,blank=True)
    new_price  = models.CharField(max_length=50)
    additional = models.TextField(blank=True)
    view       = models.IntegerField(default=0)
    Status     = models.BooleanField(default = True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products' 

class tips(models.Model):
    disease_name  = models.CharField(max_length=250)
    image         = models.ImageField(upload_to="disease/",blank=True)
    info          = models.TextField(blank=True)
    medicine1     = models.CharField(max_length=100,blank=True)
    medicine2     = models.CharField(max_length=100,blank=True)
    medicine3     = models.CharField(max_length=100,blank=True)
    medicine4     = models.CharField(max_length=100,blank=True)
    medicine5     = models.CharField(max_length=100,blank=True)
    food          = models.TextField(blank=True)
    rules         = models.TextField(blank=True)
    view          = models.IntegerField(default=0)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.disease_name
    class Meta:
        verbose_name = 'tips'
        verbose_name_plural = 'tips' 


class beauty_care(models.Model):
    tips_name  = models.CharField(max_length=250)
    image         = models.ImageField(upload_to="tips/",blank=True)
    tips        = RichTextField()
    view          = models.IntegerField(default=0)
    Status        = models.BooleanField(default = True)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.tips_name
    class Meta:
        verbose_name = 'beauty_care'
        verbose_name_plural = 'beauty_care' 


class health_care(models.Model):
    tips_name  = models.CharField(max_length=250)
    image        = models.ImageField(upload_to="tips/",blank=True)
    tips        = RichTextField()
    
    view          = models.IntegerField(default=0)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.tips_name
    class Meta:
        verbose_name = 'health_care'
        verbose_name_plural = 'health_care' 


class corona(models.Model):
    tips_name  = models.CharField(max_length=250)
    image        = models.ImageField(upload_to="tips/",blank=True)
    tips        = RichTextField()
    
    view          = models.IntegerField(default=0)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.tips_name
    class Meta:
        verbose_name = 'corona'
        verbose_name_plural = 'corona' 


class user_reg(models.Model):
    Name          = models.CharField(max_length=100)
    email         = models.EmailField(max_length=250,blank=True)
    password      = models.CharField(max_length=100)
    phone         = models.CharField(max_length=100)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Name 
    class Meta:
        verbose_name = 'user_reg'
        verbose_name_plural = 'user_reg' 


class Contact(models.Model):
    name = models.CharField(max_length=124)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact' 


class Cart(models.Model):
    product        = models.ForeignKey(product, on_delete=models.CASCADE)
    user_reg            = models.ForeignKey(user_reg, on_delete=models.CASCADE,blank=True)
    quantity       = models.IntegerField()
    price          = models.IntegerField()
    add_date      = models.DateField(auto_now=True)
    status        = models.BooleanField(default=True)
    def __str__(self):
        return str(self.product)
    class Meta:
        verbose_name='Cart'
        verbose_name_plural='Cart'