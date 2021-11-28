from django.shortcuts import render
from .models import AllProduct
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def sort_by_price(data, reverse=False):

    if len(data) <= 1:
        return data
    piv_pos = len(data)//2

    piv = data[piv_pos]

    left = []
    mid = []
    right = []

    for d in data:
        # Change compare attribute here.
        value = d.price
        piv_value = piv.price

        if not reverse:
            # from low to high
            if value < piv_value:
                left.append(d)
            elif value > piv_value:
                right.append(d)
            else:
                mid.append(d)
        else:
            # from high to low
            if value < piv_value:
                right.append(d)
            elif value > piv_value:
                left.append(d)
            else:
                mid.append(d)

    return sort_by_price(left, reverse) + mid + sort_by_price(right, reverse)


def filter_below_price(data, price):
    result = []
    for d in data:
        # Check compare value here.
        value = d.price
        if value <= price:
            result.append(d)

    return result

def product_detail_view(request,product_id):

    try:
        o = AllProduct.objects.get(id= product_id)
    except AllProduct.DoesNotExist:
        raise Http404

        
    context = {'obj':o}
    return render(request,'test_product_instance.html',context)

def product_view(request):

    # for g in request.GET:
    #     print(g,end=' ')
    #     print(request.GET[g],type(request.GET[g]))


    # desc_order = False
    # if request.GET.get('desc'):
    #     if request.GET['desc'] == 'true':
    #         desc_order = True

    # if request.GET.get('below_price'):
    #     below_price = float(request.GET.get('below_price'))
    # else:
    #     below_price = None

    # # Get all
    # allproduct = AllProduct.objects.all()

    # # Filter out
    # if below_price is not None:
    #     allproduct = filter_below_price(allproduct, below_price)

    # allproduct = sort_by_price(allproduct, desc_order)

    # context = {
    #     'allproduct': allproduct,
    # }

    return render(request, 'cases.html')

def product_view(request):

    allproducts = AllProduct.objects.all()

    context = {
        'allproducts':allproducts
    }
    return render(request,'cases.html',context)

def product_collections_view(request):
    allproducts = AllProduct.objects.all()

    context = {
        'allproducts':allproducts
    }
    return render(request,'collection.html',context)

def product_test_filter(request):
    return render(request,'product/test_product_filter.html')

def product_detail_view(request,product_id):
    obj = AllProduct.objects.get(id = product_id)

    context = {'obj':obj} 

    return render(request,'product/detail.html',context)