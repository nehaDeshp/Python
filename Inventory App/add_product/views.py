from .models import Product
from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductAdd

# Create your views here.

def displayProd(request):

    data = Product.objects.all()
    d = data.filter(product_name__contains="Pencil")
    return render(request, "display.html", {'data':data})

def prod_detail(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    return render(request, 'prodDetails.html', {'prod': prod})

def addProd(request):
    print('here')
    if request.method == 'POST':
        form = ProductAdd(request.POST)
        print("A",form)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            id = product.id
            return redirect(product,'prodDetails.html')
    else:
        form = ProductAdd()
        return render(request, 'add.html',{'form': form})
