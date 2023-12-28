from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

# Create your views here.
def SearchResult(request):
    Products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        Products=Product.objects.all().filter(Q(name__contains=query)|Q(description__contains=query))
        return render(request,'search.html',{'query':query,'products':Products})