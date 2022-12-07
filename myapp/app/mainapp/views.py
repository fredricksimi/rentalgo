from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from shop.models import (Category, 
    Product, ProductCreateForm, ProductEditForm,)



from cart.forms import CartAddProductForm
from django.utils import timezone


def home_view(request):
    items = Product.objects.all().order_by('created_at').reverse()[:4]
    return render(request, 'mainapp/home.html', {'items':items})

def checkout_view(request):
    return render(request, 'mainapp/checkout.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'mainapp/shop.html', context)
# def shop_view(request):
#     return render(request, 'mainapp/shop.html')

def product_detail(request, id, slug):
    related_products = Product.objects.all().order_by('created_at').reverse()[:4]
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'related_products':related_products
    }
    return render(request, 'mainapp/product-detail.html', context)




@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            befo = form.save(commit=False)
            befo.owner = request.user
            befo.created_at = timezone.now()
            befo.save()
            return redirect('mainapp:your-account')

    else:
        form = ProductCreateForm()
    context = {
        'form':form,
    }
    return render(request, 'mainapp/product-create.html', context)


@login_required
def product_edit(request, id):
    the_product = get_object_or_404(Product, id=id)
    if request.user != the_product.owner:
        return redirect('mainapp:home')

    else:
        if request.method == 'POST':
            form = ProductEditForm(request.POST, request.FILES, instance=the_product)
            if form.is_valid():
                bell = form.save(commit=False)
                bell.owner = request.user
                bell.save()
                return redirect('mainapp:your-account')
        else:
            form = ProductEditForm(instance=the_product)
        context = {
        'form':form
        }

        return render(request, 'mainapp/product-edit.html', context)

@login_required
def product_delete(request, id):
    d_product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        d_product.delete()
        return redirect('mainapp:your-account')
    context={
    'd_product':d_product
    }
    return render(request, 'mainapp/delete-confirmation.html', context)



def cart_view(request):
    return render(request, 'mainapp/cart.html')

def contact_view(request):
    return render(request, 'mainapp/contact.html')

def terms_view(request):
	return render(request, 'mainapp/terms.html')

@login_required
def youraccount_view(request):
    produ = Product.objects.all()
    pro = produ.filter(owner__username=request.user.username).last()
    your_products = Product.objects.all().filter(owner__username=request.user.username).order_by('-created_at')
    context = {
        'your_products':your_products,
        'pro':pro
    }
    return render(request, 'mainapp/youraccount.html', context)

