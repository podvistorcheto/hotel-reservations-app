from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testing')
        else:
            return render(request, 'dates.html', {'form': form})
    else:
        return render(request, 'dates.html', {'form': ProductForm()})
