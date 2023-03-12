from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import Http404

from .carrello import Carrello
from store.models import Product
# Create your views here.

def carrello_content(request):
    #print(request)
    #print("carrello loaded from carrello_content")
    carrello = Carrello(request)
    return render(request, 'store/carrello/content.html')

def carrello_add(request):
    print(request)

    carrello = Carrello(request)
    if request.POST.get('action') == 'post':
        productID = int(request.POST.get('productID'))
        product_amount = int(request.POST.get('amount'))
        product = get_object_or_404(Product, id=productID)
        carrello.insert(product=product, amount=product_amount)

        total = carrello.__len__()
        
        response = JsonResponse({'amount': total})
        return response
    
def carrello_remove(request):
    print(request)
    carrello = Carrello(request)
    if request.POST.get('action') == 'post':
        id = int(request.POST.get('productID'))
        carrello.removeItem(item=id)
        
        basketqty = carrello.__len__()
        baskettotal = carrello.get_tot()
        round(baskettotal,2)
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        #response = JsonResponse({'success': True})
        return response




