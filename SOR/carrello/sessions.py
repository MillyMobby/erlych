from .carrello import Carrello

def carrello(request):
    print(request)
    return {'carrello': Carrello(request)}