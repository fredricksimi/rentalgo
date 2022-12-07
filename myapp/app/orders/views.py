from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                ) 
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})



# @login_required
# def profileupdateview(request):
# 	if request.method == 'POST':
# 		profile_form = ProfileUpdateForm(instance=request.user.profile, data=request.POST, files=request.FILES)
# 		if profile_form.is_valid():
# 			profile_form.save()
# 			return redirect('mainapp:your-account')
# 	else:
# 		profile_form = ProfileUpdateForm(instance=request.user.profile)
# 	return render(request, 'mainapp/youraccount-update.html', {'profile_form':profile_form})
