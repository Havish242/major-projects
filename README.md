# 🛍️ M webstore (Django)

This is a **Django-based E-Commerce Website** that allows users to browse products, add them to a cart, and place orders.  
It uses **Django Models** to handle products, categories, users, orders, and cart functionality.

---

## 🚀 Features

- 🔐 **User Authentication** – Register, login, logout, and manage profile  
- 🛒 **Product Catalog** – View products by category, brand, or price  
- 🛍️ **Shopping Cart** – Add, update, and remove items from the cart  
- 💳 **Checkout** – Place orders with delivery details  
- ⭐ **Reviews & Ratings** – Customers can rate and review products  
- 📦 **Admin Dashboard** – Manage products, categories, orders  

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)  
- **Database**: SQLite (default), supports PostgreSQL/MySQL  
- **Frontend**: HTML, CSS, Bootstrap  
- **Other Tools**: Django Admin  

---

## 📂 Project Structure

ecommerce/
│
├── ecommerce/ # Main Django project folder
│ ├── settings.py # Project settings
│ ├── urls.py # URL routing
│ └── ...
│
├── store/ # Django app for products, cart, orders
│ ├── models.py # Database models
│ ├── views.py # Business logic
│ ├── urls.py # App-level URLs
│ ├── templates/ # HTML templates
│ └── static/ # CSS, JS, images
│
├── manage.py
└── requirements.txt


---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Havish242/major-projects.git
   cd major-projects/ecommerce


Create a virtual environment & activate

python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py makemigrations
python manage.py migrate


Create a superuser (for admin panel)

python manage.py createsuperuser


Run the development server

python manage.py runserver


Open your browser at:
👉 http://127.0.0.1:8000

🖥️ Screenshots

(Add your screenshots here: Homepage, Product Page, Cart, Checkout, Admin Dashboard)

📌 Future Improvements

✅ Payment gateway integration (Razorpay, Stripe, PayPal)

✅ Wishlist & Favorites

✅ Recommendation system

✅ Advanced search & filtering

📄 License

This project is licensed under the MIT License – feel free to use and modify.

👨‍💻 Author

Developed by Havish
 ✨


---

## 📄 `requirements.txt`

```txt
Django>=4.2
djangorestframework>=3.14
Pillow>=10.0
django-crispy-forms>=2.0
crispy-bootstrap5>=0.7

📌 Future Improvements

✅ Payment gateway integration (Razorpay, Stripe, PayPal)

✅ Wishlist & Favorites

✅ Recommendation system

✅ Advanced search & filtering



