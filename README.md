# Box Selection API 📦

## Project Overview

The **Box Selection API** is a Django-based backend system designed to optimize ecommerce warehouse operations.

When a customer places an order, the system evaluates the product’s **dimensions** and **weight**, compares them against available shipping boxes, and recommends the **most cost-effective box** capable of safely containing the product.

The system uses a **3D bin-packing inspired algorithm** that considers **spatial rotation of products** before selecting the optimal shipping box.

This helps reduce packaging waste, improve warehouse efficiency, and optimize shipping cost.

---

# Problem Statement

For an ecommerce platform, warehouse staff must decide which shipping box should be used for every customer order.

Each:

### Product contains:

* Name
* Length
* Width
* Height
* Weight

### Box contains:

* Internal Length
* Internal Width
* Internal Height
* Maximum Weight Capacity
* Cost

The system must:

1. Validate weight compatibility
2. Check whether product dimensions fit inside box
3. Support 3D spatial rotation
4. Select cheapest valid box
5. Return error if no suitable box exists

---

# Tech Stack

* **Language:** Python 3.12
* **Framework:** Django 6.0.6
* **API Framework:** Django REST Framework (DRF)
* **Database:** SQLite3
* **Testing:** Django Test Framework + DRF APIClient
* **Version Control:** Git + GitHub
* **CI/CD:** GitHub Actions

---

# Project Structure

```text
ecommerce_shipping/
│
├── ecommerce_shipping/          # Project settings
│
├── box_selector/               # Main application
│   ├── models.py              # Product and Box models
│   ├── services.py            # Box recommendation algorithm
│   ├── serializers.py         # API serializers
│   ├── views.py              # API business logic
│   ├── urls.py               # API routes
│   ├── tests.py             # Automated test cases
│   └── admin.py            # Django admin configuration
│
├── requirements.txt
├── README.md
├── AI_USAGE.md
└── TEST_OUTPUT.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

For Linux/macOS:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Used for Django admin panel.

---

# Running Development Server

```bash
python manage.py runserver
```

Server:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

# Core Algorithm Logic

The box recommendation algorithm follows four major steps.

## Step 1 — Filter by Weight

Select boxes where:

```text
box.max_weight_capacity >= product.weight
```

---

## Step 2 — Handle 3D Rotation

Products may be rotated before packaging.

Sort dimensions before comparison.

Example:

```text
Product Dimensions = [10, 5, 2]
Sorted Product = [2, 5, 10]

Box Dimensions = [5, 12, 3]
Sorted Box = [3, 5, 12]
```

Condition:

```text
product_dimension <= box_dimension
```

---

## Step 3 — Cost Optimization

If multiple boxes fit:

```text
Return cheapest box
```

Sorted by:

```text
cost (ascending)
```

---

## Step 4 — Failure Handling

If no valid box exists:

```text
Return error response
```

---

# API Reference

## Get Box Recommendation

Returns the cheapest valid box for a product.

### Endpoint

```text
/api/box-selector/recommend-box/<product_id>/
```

### Method

```text
GET
```

---

## Success Response (200 OK)

```json
{
    "message": "Optimal box found.",
    "recommended_box": {
        "id": 1,
        "name": "Small Box",
        "internal_length": "5.00",
        "internal_width": "12.00",
        "internal_height": "3.00",
        "max_weight_capacity": "5.00",
        "cost": "1.50"
    }
}
```

---

## Error Response (404 Not Found)

```json
{
    "error": "No suitable box exists that can fit product 'Anvil'."
}
```

---

# Database Models

## Product Model

```python
Product
- name
- length
- width
- height
- weight
```

---

## Box Model

```python
Box
- name
- internal_length
- internal_width
- internal_height
- max_weight_capacity
- cost
```

---

# Automated Testing

The project contains **8 automated test cases**.

Run tests:

```bash
python manage.py test box_selector
```

Actual terminal output:

```text
(venv) PS C:\all codes\Desktop\Box_Selection_System\ecommerce_shipping> python manage.py test box_selector

Found 8 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).

........

----------------------------------------------------------------------
Ran 8 tests in 0.090s

OK

Destroying test database for alias 'default'...
```

---

# Test Coverage

Implemented automated tests for:

1. Successful box recommendation
2. No suitable box available
3. Invalid product ID returns 404
4. Cheapest valid box selected
5. 3D rotation logic validation
6. Exact weight boundary validation
7. No boxes available in database
8. API response structure validation

---

# Example Database Test Data

Boxes:

```text
Small Box
Medium Box
Large Box
```

Products:

```text
Smartphone
Heavy Product (Anvil)
Boundary Product
Rotated Product
```

---

# Django Admin Panel

Admin panel configured for database management.

Manage:

* Products
* Boxes

Access:

```text
http://127.0.0.1:8000/admin/
```

---

# CI/CD Pipeline

GitHub Actions configured for Continuous Integration.

On every:

* Push to main branch
* Pull request

Pipeline automatically:

1. Creates Ubuntu runner
2. Installs dependencies
3. Runs migrations
4. Executes Django tests
5. Prevents broken code merge

---

# Additional Documentation

This project includes:

```text
README.md         → Project documentation
AI_USAGE.md       → AI usage tracking
TEST_OUTPUT.md    → Testing and terminal verification logs
```

---

# Features Implemented

✓ Django Backend Setup
✓ Product Model
✓ Box Model
✓ 3D Rotation Algorithm
✓ Weight Capacity Validation
✓ Cheapest Box Selection Logic
✓ REST API Endpoint
✓ Django Admin Panel
✓ SQLite Database
✓ Automated Testing
✓ API Testing
✓ GitHub Actions CI/CD

---

# Future Improvements

Possible enhancements:

* Frontend dashboard
* Multi-product order support
* PostgreSQL integration
* Docker deployment
* Cloud deployment

---

# Author

**Yash Jagtap**

Engineering Student | Backend Developer | Python Developer

## What I Learned ?

While making this project, 
I learned many things about backend development using Django in a practical way. The main thing I understood was 3D sorting logic. I learned that when a product can rotate in different directions, checking dimensions directly is not enough, so sorting dimensions first gives more correct results.
I also learned how to create APIs using Django REST Framework, how to write test cases, and how to solve errors when code gives problems. 
This project taught me that development is not only about coding, but also about thinking logically, testing every part, and solving issues one by one.

