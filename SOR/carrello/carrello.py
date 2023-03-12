from decimal import Decimal
from store.models import Product
class Carrello():

    def update(self, item, amount):
        pID = str(item)
        if pID in self.carrello:
            self.carrello[pID]['amount'] = amount
        self.session.modified = True  
    

    def removeItem(self, item):
        id = str(item)
        print(type(id))
        if id in self.carrello:             
            del self.carrello[id]
            
            self.session.modified = True  

        
    #quando user spedisce dati dal browser (http request), i dati sono in request, also per la session se esiste
    def __init__(self, request):
        print(request)
        self.session = request.session #leggere documentazione sulle session di django
        carrello = self.session.get('skey')
        if 'skey' not in request.session:
            carrello = self.session['skey'] = {}
        self.carrello = carrello


    def insert(self, product, amount):
        productID = product.id
        if productID not in self.carrello:
            self.carrello[productID] = {'price': float(product.price), 'amount': int(amount)}  #lo inserisco se non è nel carrello

        self.session.modified = True  #modified è un comando per aggiornare la sessione

    def __len__(self):
        return sum(item['amount'] for item in self.carrello.values())

    def __iter__(self):
        product_dictionary = self.carrello.keys()
        products = Product.products.filter(id__in=product_dictionary)
        carrello = self.carrello.copy()

        for product in products:
            carrello[str(product.id)]['product'] = product

        for item in carrello.values():
            item['price'] = item['price']
            item['total_price'] = item['price']*item['amount']
            yield item

    def get_tot(self):
        result = sum((item['price']) * item['amount'] for item in self.carrello.values())
        result = round(result,2)
        return result
