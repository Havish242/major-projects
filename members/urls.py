from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, MemberViewSet, OrderViewSet, OrderItemViewSet, home, category_list, category_detail, product_list, product_detail, add_category, add_product

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'members', MemberViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
	path('', home, name='home'),
	path('categories/', category_list, name='category-list'),
	path('categories/add/', add_category, name='add-category'),
	path('categories/<int:category_id>/', category_detail, name='category-detail'),
	path('products/', product_list, name='product-list'),
	path('products/add/', add_product, name='add-product'),
	path('products/<int:product_id>/', product_detail, name='product-detail'),
] + router.urls