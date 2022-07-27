from django.urls import path
from . import views
urlpatterns = [
    path('',views.get_product_order , name='cart'),
    path('add',views.add_product , name='add'),
    path('remove',views.remove_product,name="remove"),
]