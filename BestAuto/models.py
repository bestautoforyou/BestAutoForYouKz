from django.db import models
from django.db.models import Model
from django.utils import timezone
from PIL import Image
from django.urls import reverse

class Products(models.Model):
    pname = models.CharField(max_length=100)
    pcategory = models.CharField(max_length=100)# Car Parts, Coins, Bones
    pprice = models.CharField(max_length=100)
    pdescription = models.CharField(max_length=500)
    pimage = models.ImageField(default='default.jpg', upload_to='product_pics')
    pdate_posted = models.DateTimeField(default=timezone.now)
    poffer = models.BooleanField(default=False)
    # pallimages = models.FileField(upload_to='product_pics')



    def save(self):
        super().save()

        img = Image.open(self.pimage.path)

        if img.height > 300 or img.width > 300 or img.height < 300 or img.width < 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pimage.path)



    def __str__(self):
        return self.pname
    #
    #
    def get_absolute_url(self):
        return reverse('products-individual', kwargs={'pk': self.pk})





class ProductsImage(models.Model):
    pioriginal = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    piimages = models.FileField(upload_to='product_pics')

    def save(self):
        super().save()

        img = Image.open(self.piimages.path)

        if img.height > 300 or img.width > 300 or img.height < 300 or img.width < 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.piimages.path)

    def __str__(self):
        return self.pioriginal.pname
    def get_absolute_url(self):
        return reverse('products-individual', kwargs={'pk': self.pioriginal.pk})







class Contact(models.Model):
  name = models.CharField(max_length=122)
  email = models.EmailField(max_length=120)
  subject = models.TextField()
  message = models.TextField()
  # code to show name of the person who sent you the message
  def _str_(self):
    return self.name