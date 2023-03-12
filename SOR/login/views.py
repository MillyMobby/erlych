from django.shortcuts import render
from .forms import Register
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.shortcuts import get_object_or_404
from .tokens import account_activation_token
from .wishlist import Wishlist
from store.models import Product
from .models import Account

def add_to_wishlist(request):
    print(request)

    wishlist = Wishlist(request)
    if request.POST.get('action') == 'post':
        productID = int(request.POST.get('productID'))
        product_amount = int(request.POST.get('amount'))
        product = get_object_or_404(Product, id=productID)
        wishlist.insert(product=product, amount=product_amount)

        total = 0 #wishlist.__len__()
        
        response = JsonResponse({'amount': total})
        return response
    

def wishlist_content(request):
    wishlist = Wishlist(request)
    return render(request, 'users/.html')

def wishlist_remove(request):
    print(request)
    wishlist = Wishlist(request)
    if request.POST.get('action') == 'post':
        id = int(request.POST.get('productID'))
        wishlist.removeItem(item=id)
        
        number = wishlist.__len__()
        total = wishlist.get_tot()
        response = JsonResponse({'qty': number, 'subtotal': total})
        #response = JsonResponse({'success': True})
        return response


# Create your views here.
def user_registration(request):

    if request.user.is_authenticated:
        return redirect('login:dashboard')
    
    if request.method == 'POST':
        registerForm = Register(request.POST)
        if registerForm.is_valid():
            costumer = registerForm.save(commit=False)
            costumer.email = registerForm.cleaned_data['email']
            costumer.set_password(registerForm.cleaned_data['password'])
            costumer.is_active = False
            costumer.save()
            sito_web = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('users/email.html', {
                'user': costumer,
                'domain': sito_web.domain,
                'uid': urlsafe_base64_encode(force_bytes(costumer.pk)), #user identifier
                'token': account_activation_token.make_token(costumer),
            })
            costumer.email_user(subject=subject, message=message)
            return HttpResponse('è stata inviata una mail di verifica')
        else:
            return redirect('login:invalid')
            # return HttpResponse(' NOT registered USER ')
    else:
        subscription = Register()
        return render(request, 'users/subscribe.html', {'form': subscription})
    
@login_required
def dashboard(request):
    return render(request,
                  'users/accountPage.html')

def invalid_registration(request):
    return render(request,
                  'users/invalidRegistration.html')

def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        pass
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('login:dashboard')
    else:
        return HttpResponse('registered grrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr GOOD USER ')
 
