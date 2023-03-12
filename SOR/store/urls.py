from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    
    path('', views.all_products, name='all_products'),
    path('all', views.all_products_categories, name='all_products_categories'),
    path('artists', views.all_artists, name='all_artists'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:genre_slug>/', views.genre_list, name='genre_list'),

    path('<slug:artist_slug>', views.artist_list, name='artist_list'),
]

# <slug:slug> -> <tipoDiDato:nomeDato>