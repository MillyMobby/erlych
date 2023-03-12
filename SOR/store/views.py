from django.shortcuts import get_object_or_404, render

#get_object_or_404 = shortcut per accedere ai dati del database

from .models import Genre, Artist, Product

def genres(request):
    return {
        'genres': Genre.objects.all()
    }

def artists(request):
    return {
        'artists': Artist.objects.all()
    }


def all_products_categories(request):
    products = Product.products.all()
    return render(request, 'store/allProducts.html', {'products': products})

def all_artists(request):
    artists = Artist.objects.order_by("name")
    return render(request, 'store/allArtists.html', {'artists': artists})

def all_products(request):
    products = Product.products.filter(pk__in=[1, 2, 3, 4, 5])  #sono gli album mostrati nella home
    return render(request, 'store/home.html', {'products': products})

def new_products(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'products/detail.html', {'product': product})







def genre_list(request, genre_slug=None):
    genre = get_object_or_404(Genre, slug=genre_slug) 
    products = Product.objects.filter(genre=genre)
    return render(request, 'products/category.html', {'genre': genre, 'products': products})

def artist_list(request, artist_slug):
    artist = get_object_or_404(Artist, slug=artist_slug) 
    products = Product.objects.filter(artist=artist)
    return render(request, 'products/artist.html', {'artist': artist, 'products': products})







