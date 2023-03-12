from django.urls import path 
from . import views 

app_name = 'carrello'

urlpatterns = [
    path('', views.carrello_content, name='carrello_content'),
    path('add/', views.carrello_add, name='carrello_add'),    
    path('remove/', views.carrello_remove, name='carrello_remove'),
    #path('update/', views.carrello_update, name='carrello_update'),
]