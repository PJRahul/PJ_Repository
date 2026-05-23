from django.shortcuts import render

from .forms import OrderForm

# Create your views here.
def home(request):
    return render(request, 'pizza\home.html')

def order(request):
    if request.method == 'POST':
        ODR = OrderForm(request.POST, request.FILES)
        if ODR.is_valid():
            # Process the form data
            name = ODR.cleaned_data['name']
            description = ODR.cleaned_data['description']
            size = ODR.cleaned_data['size']
            price = ODR.cleaned_data['price']
            toppings = ODR.cleaned_data['toppings']
            image = ODR.cleaned_data['image']
            notes = f"Order received: {name}, {description}, {size}, {price}, {toppings}, {image}"
            newform = OrderForm()
            return render(request, 'pizza\order.html', {'form': newform, 'notes': notes})   
    else:
        ODR = OrderForm()
    return render(request, 'pizza\order.html', {'form': ODR})