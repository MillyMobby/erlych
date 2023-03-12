from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

from .forms import SignIn
#per richiamare gli url --> namespace_app:nome_url
app_name = 'login'

urlpatterns = [
     path('login/', auth_views.LoginView.as_view(template_name='users/login.html', form_class=SignIn), name='login'),
     path('logout/', auth_views.LogoutView.as_view(next_page='/login/login/'), name='logout'),
     path('register/', views.user_registration, name='register'),
     path('invalid/', views.invalid_registration, name='invalid'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
     path('wishlist/', views.wishlist_content, name='wishlist'),
     path('add/', views.add_to_wishlist, name='add_to_wishlist'),    
     path('remove/', views.wishlist_remove, name='wishlist_remove'),
]
