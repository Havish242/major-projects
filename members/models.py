
from django.db import models

# Category model
class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name
class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
	stock = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name
class Member(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	address = models.TextField(blank=True)

	def __str__(self):
		return self.name

# Order model
class Order(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='orders')
	created_at = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=20, default='pending')

	def __str__(self):
		return f"Order {self.id} by {self.member.name}"

# OrderItem model
class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return f"{self.quantity} x {self.product.name}"
from django.db import models
