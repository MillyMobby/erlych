from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.conf import settings
#reverse -> permette di costruire un url
#templates dati a django per creare il database

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Genre(models.Model): #FIRST TABLE
    name = models.CharField(max_length=255, db_index=True) ##cercare documentazione!!!!!!!!!!!!
    slug = models.SlugField(max_length=255, unique=True)  
     #SLUGS ---> per mostrare categoria da mostrare nel sito, sono delle etichette che vanno negli urls 
    class Meta:
        verbose_name_plural = 'genres' #nome plurale per le categorie del database
    
    def get_absolute_url(self):
        return reverse('store:genre_list', args=[self.slug])

    def __str__(self):
        return self.name     
    


class Artist(models.Model): #FIRST TABLE
    name = models.CharField(max_length=255, db_index=True) 
    slug = models.SlugField(max_length=255, unique=True)  
    picture = models.ImageField(upload_to='images/')
    biography = models.TextField(blank=True)
    
     #SLUGS ---> per mostrare categoria da mostrare nel sito, come le directory nella shell
                  #no special characters, nome unico    
    class Meta:
        verbose_name_plural = 'artists' #nome plurale per le categorie
    
    def get_absolute_url(self):
        return reverse('store:artist_list', args=[self.slug])

    def __str__(self):
        return self.name     


class Product(models.Model):   
    genre = models.ForeignKey(Genre, related_name='product', on_delete=models.CASCADE) #related_name='product'
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin_creator')
    title = models.CharField(max_length=255)
    #artist = models.CharField(max_length=255, default='admin')
    artist = models.ForeignKey(Artist, related_name='product', on_delete=models.CASCADE) 
    summary = models.TextField(blank=True)
    overview = models.TextField(blank=True)
    cover = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)  
    price = models.DecimalField(max_digits=4, decimal_places=2)
    available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products' #nome plurale per le categorie
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])  #per buildare secondo path in urls.py nella lista urlspatterns[]
                                        #product_detail=    name nella path in urls.py
  
    def __str__(self):
        return self.title  
    

