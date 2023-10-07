
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def index(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'Kanemisan/index.html', context)
