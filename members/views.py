from rest_framework import viewsets
from .models import Category, Product, Member, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, MemberSerializer, OrderSerializer, OrderItemSerializer
from rest_framework import viewsets
from .models import Category, Product, Member, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, MemberSerializer, OrderSerializer, OrderItemSerializer

from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CategoryForm, ProductForm

def home(request):
	categories = Category.objects.all()
	products = Product.objects.all()[:6]  # Show 6 featured products
	return render(request, 'members/home.html', {'categories': categories, 'products': products})


def category_list(request):
	categories = Category.objects.all()
	return render(request, 'members/category_list.html', {'categories': categories})

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('category-list')
	else:
		form = CategoryForm()
	return render(request, 'members/add_category.html', {'form': form})


def category_detail(request, category_id):
	category = Category.objects.get(id=category_id)
	products = Product.objects.filter(category=category)
	return render(request, 'members/category_detail.html', {'category': category, 'products': products})

def product_list(request):
	products = Product.objects.all()
	return render(request, 'members/product_list.html', {'products': products})

def add_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('product-list')
	else:
		form = ProductForm()
	return render(request, 'members/add_product.html', {'form': form})


def product_detail(request, product_id):
	product = Product.objects.get(id=product_id)
	return render(request, 'members/product_detail.html', {'product': product})
class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class MemberViewSet(viewsets.ModelViewSet):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer

class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemSerializer
     