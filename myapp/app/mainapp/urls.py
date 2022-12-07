from django.urls import path
from . import views
from users import views as userviews

app_name = 'mainapp'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('shop', views.product_list, name='shop'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    path('product-create', views.product_create, name='product-create'),
    path('product-edit/<int:id>/', views.product_edit, name='product-edit'),
    path('product-delete/<int:id>/', views.product_delete, name='product-delete'),


    path('cart', views.cart_view, name='cart'),
    path('checkout', views.checkout_view, name='checkout'),
    path('contact', views.contact_view, name='contact'),
    path('terms', views.terms_view, name='terms'),

    
    path('your-account', views.youraccount_view, name='your-account'),
    path('first-account-update', userviews.profilefirstupdateview, name='first-account-update'),
    path('account-update', userviews.profileupdateview, name='account-update')
]
