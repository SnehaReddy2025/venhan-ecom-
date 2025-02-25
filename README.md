# Project Name
Order Management API

## Description
This is a backend API built using FastAPI and MongoDB to manage orders. It includes user authentication, order creation, updates, and retrieval.
## Features

User authentication (JWT-based).
Product creation, updating, and retrieval
Order creation, updating, and retrieval.
MongoDB for data storage.
Error handling and validation.
Uses Pydantic models for request and response validation.

## Project Structure

/app  
│── /api/v1/routes      # API route handlers  
│── /services           # Business logic functions  
│── /models             # Pydantic models  
│── /db                 # Database connection  
│── /utils              # Utility functions  
│── main.py             # Entry point of the application  
│── config.py           # Configuration settings  
│── requirements.txt    # Python dependencies  


## API Endpoints

# Authentication
POST [/api/v1/auth/register](http://localhost:8020/api/v1/auth/signup) → Register a new user
POST [/api/v1/auth/login](http://localhost:8020/api/v1/auth/login) → Log in and get a JWT token

# Products

POST [/api/v1/products/](http://localhost:8020/api/v1/products) → Create a new product
GET [/api/v1/products/ ](http://localhost:8020/api/v1/products)→ Get all products
GET [/api/v1/products/{product_id}](http://localhost:8020/api/v1/products/{product_id}) → Get product details
PUT [/api/v1/products/{product_id}](http://localhost:8020/api/v1/products/{product_id}) → Update a product
DELETE [/api/v1/products/{product_id}](http://localhost:8020/api/v1/products/{product_id}) → Delete a product

# Orders

POST [/api/v1/orders/](http://localhost:8020/api/v1/orders/) → Create a new order
GET [/api/v1/orders/ ](http://localhost:8020/api/v1/orders/)→ Get all Orders
GET [/api/v1/orders/{order_id}](http://localhost:8020/api/v1/orders/(order_id)) → Get order details
PUT [/api/v1/orders/{order_id} ](http://localhost:8020/api/v1/orders/(order_id))→ Update an order




```bash
# Clone the repository
git clone https://github.com/yourusername/yourproject.git

# Navigate to the project directory
cd yourproject

# Install dependencies
pip install -r .\requirements.txt
```

```bash
# Start the development server
python -m app.main
```

## Contributing
Guidelines for contributing to the project.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.


## Contact
Sneha Bandla- [snehareddy2025@gmail.com](mailto:snehareddy2025@gmail.com)
