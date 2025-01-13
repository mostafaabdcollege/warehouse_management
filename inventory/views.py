from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Supplier, StockTransaction
from django.core.exceptions import ValidationError
from decimal import Decimal, InvalidOperation
from django.contrib import messages

# Home Page
def home(request):
    return render(request, 'home.html')

# List Products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

# Add Product
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        if name and quantity and price:
            try:
                price = Decimal(price)  
                if price < 0:
                    raise ValidationError("Price cannot be negative.")

                Product.objects.create(
                    name=name,
                    description=description,
                    quantity=quantity,
                    price=price,
                    image=image
                )
                messages.success(request, "Product added successfully!")
                return redirect('product_list')
            except (ValueError, InvalidOperation):
                messages.error(request, "Invalid price entered. Please enter a valid number.")
            except ValidationError as e:
                messages.error(request, str(e))

    return render(request, 'inventory/add_product.html')

# Edit Product
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.quantity = request.POST.get('quantity')
        product.price = request.POST.get('price')
        if 'image' in request.FILES:
            product.image = request.FILES.get('image')
        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect('product_list')

    return render(request, 'inventory/edit_product.html', {'product': product})

# Delete Product
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('product_list')

# List Suppliers
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/supplier_list.html', {'suppliers': suppliers})

# Add Supplier
def add_supplier(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        email = request.POST.get('email')

        Supplier.objects.create(
            name=name,
            contact_number=contact_number,
            address=address,
            email=email
        )
        messages.success(request, "Supplier added successfully!")
        return redirect('supplier_list')

    return render(request, 'inventory/add_supplier.html')

# Edit Supplier
def edit_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.name = request.POST.get('name')
        supplier.contact_number = request.POST.get('contact_number')
        supplier.address = request.POST.get('address')
        supplier.email = request.POST.get('email')
        supplier.save()
        messages.success(request, "Supplier updated successfully!")
        return redirect('supplier_list')

    return render(request, 'inventory/edit_supplier.html', {'supplier': supplier})

# Delete Supplier
def delete_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    messages.success(request, "Supplier deleted successfully!")
    return redirect('supplier_list')

# List Transactions
def transaction_list(request):
    transactions = StockTransaction.objects.all()
    return render(request, 'inventory/transaction_list.html', {'transactions': transactions})

# Add Stock Transaction
def add_transaction(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        transaction_type = request.POST.get('transaction_type')
        quantity = request.POST.get('quantity')

        product = get_object_or_404(Product, pk=product_id)

        if transaction_type == 'OUT' and product.quantity < int(quantity):
            messages.error(request, "Not enough stock available!")
        else:
            StockTransaction.objects.create(
                product=product,
                transaction_type=transaction_type,
                quantity=quantity
            )
            if transaction_type == 'IN':
                product.quantity += int(quantity)
            else:
                product.quantity -= int(quantity)
            product.save()
            messages.success(request, "Transaction added successfully!")
            return redirect('transaction_list')

    products = Product.objects.all()
    return render(request, 'inventory/add_transaction.html', {'products': products})

# Custom 404 Error Page
def custom_404_view(request, exception):
    return render(request, 'inventory/404.html', status=404)

# Custom 500 Error Page
def custom_500_view(request):
    return render(request, 'inventory/500.html', status=500)
