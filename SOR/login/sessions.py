from .wishlist import Wishlist

def wishlist(request):
    print(request)
    return {'wishlist': Wishlist(request)}