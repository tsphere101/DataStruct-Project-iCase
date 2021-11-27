from django.urls import path
from .views import product_view,product_test_view,product_collections_view



urlpatterns = [
    
    path('',product_view,name='cases') ,
    path('collection/',product_collections_view,name='collection'),
    path('test/',product_test_view,name = 'cases_test')
    
]