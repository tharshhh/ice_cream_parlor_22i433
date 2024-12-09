# ice_cream_parlor_22i433
Simple python application for a fictional ice cream parlor cafe using SQLite
# Ice Cream Delivery System

## Project Overview

This is a web application designed for managing an ice cream delivery service. It allows users to place orders, view available ice cream flavors, and track deliveries. The backend is built using Flask, while the frontend is created with HTML and CSS. The application provides a simple and user-friendly interface for customers to order ice cream and track their orders in real-time.

## Features

- User-friendly interface for browsing available ice cream flavors.
- Ability to place orders and track delivery status.
- Admin dashboard for managing ice cream flavors and orders.
- Basic authentication for users and admins.

## Project Structure
ice_cream_parlor/
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── db.py
│   ├── models.py
│   └── routes.py
├── static/
│   └── styles.css
├── templates/
│   ├── home.html
│   ├── add_product.html
│   ├── edit_product.html
│   ├── delete_product.html
│   └── view_products.html
├── requirements.txt
└── run.py


## Prerequisites

To run this project, you'll need the following installed on your system:

- Python 3.x
- pip (Python package installer)

## Installation Instructions

1. **Clone the Repository:**
   First, clone the project repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/icecream-delivery.git
   cd icecream-delivery
2. Set up virtual environment
 python -m venv venv

3. Install dependencies
   pip install -r requirements.txt

4. Set up database
from app import db
db.create_all()

5. Run app
 python run.py





