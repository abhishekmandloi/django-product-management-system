from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('index', views.index, name='index'),
    path('bill', views.add_bill, name='bill'),
    path('billtest', views.add_billtest, name='billtest'),
    path('', views.dashboard, name='dashboard'),
    path('add_customer', views.add_customer, name='add_customer'),
    path('add_product_packing', views.add_product_packing, name='add_product_packing'),
    path('add_product', views.add_product, name='add_product'),
    path('add_product_ingredient', views.add_product_ingredient, name='add_product_ingredient'),
    path('add_product_batch', views.add_product_batch, name='add_product_batch'),
    path('edit_customer/<int:pk>', views.edit_customer, name='edit_customer'),
    path('edit_ingredient/<int:pk>', views.edit_ingredient, name='edit_ingredient'),
    path('edit_product_packing/<int:pk>', views.edit_product_packing, name='edit_product_packing'),
    path('edit_product/<int:pk>', views.edit_product, name='edit_product'),
    path('edit_product_batch/<int:pk>', views.edit_product_batch, name='edit_product_batch'),
    path('delete_ingredient/<int:pk>', views.delete_ingredient, name='delete_ingredient'),
    path('delete_customers/<int:pk>', views.delete_customers, name='delete_customers'),
    path('delete_product_batch/<int:pk>', views.delete_product_batch, name='delete_product_batch'),
    path('delete_product_packing/<int:pk>', views.delete_product_packing, name='delete_product_packing'),
    path('delete_product/<int:pk>', views.delete_product, name='delete_product'),
    path('delete_order/<int:pk>', views.delete_order, name='delete_order'),
    path('customers', views.customers, name='customers'),
    path('product_packing', views.product_packing, name='product_packing'),
    path('product', views.product, name='product'),
    path('product_ingredient', views.product_ingredient, name='product_ingredient'),
    path('product_batch', views.product_batch, name='product_batch'),
    path('expired_product', views.expired_product, name='expired_product'),
    path('show/<int:purchaseno>', views.show, name='show'),
    path('edit/<int:purchaseno>/<int:customer_id>', views.edit_billtest_final, name='edit'),
]
