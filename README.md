Simple CRUD Django REST API Demo

This project is a straightforward demonstration of a CRUD (Create, Read, Update, Delete) API built using Django and Django REST Framework. It showcases essential functionalities for managing products, including retrieving, creating, updating, and deleting product entries.
Features

    Get Products: Retrieve a list of all products or receive a message if no products are found.
    Create Product: Add a new product with details such as name and price.
    Product Details: Retrieve, update, or delete a specific product using its primary key (PK).
    Easy-to-understand code structure: Ideal for learning and quick integration.
    Basic validation and error handling: Ensures data integrity and provides meaningful error messages.

Getting Started
Prerequisites

    Python 3.12.4
    Django 5.1.2
    Django REST Framework

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/simple-crud-django-rest-api-demo.git
cd simple-crud-django-rest-api-demo

Install the required packages:

bash

pip install -r requirements.txt

Run migrations to set up the database:

bash

python manage.py migrate

Create a super admin account:

bash

python manage.py createsuperuser

Follow the prompts to set up the username, email, and password for the admin account. Once created, you can access the Django admin interface to manage products.

Start the development server:

bash

    python manage.py runserver

    Explore the API endpoints at http://localhost:8000/api/products/.

Usage

Use tools like Postman or cURL to test the API endpoints for managing products. Here are some examples of requests you can make:

    GET /api/products/ - Retrieve a list of all products.
    POST /api/products/create/ - Create a new product (send JSON data).
    GET /api/products/<int:pk>/ - Retrieve details of a specific product.
    PUT /api/products/<int:pk>/ - Update a specific product (send JSON data).
    DELETE /api/products/<int:pk>/ - Delete a specific product.

Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
