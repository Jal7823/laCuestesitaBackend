# Django Project 🏗️

## Overview

This is a Django project that includes several applications to manage a beverage system, ingredients, dishes, users, and categories. The API is built using Django REST Framework (DRF) for CRUD operations.

## Frontend Integration

This backend will be used by a frontend built with [React](https://reactjs.org/) ⚛️, [Vite](https://vitejs.dev/) 🚀, and [Tailwind CSS](https://tailwindcss.com/) 🌊.


## Project Structure

The project is organized into the following applications:

- **drinks** 🍹: Management of beverages.
- **ingredients** 🥕: Management of ingredients.
- **plates** 🍽️: Management of dishes, including relationships with ingredients and categories.
- **users** 👤: User management and authentication.
- **categories** 📋: Management of categories for dishes.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- Mysql
- Other packages listed in `requirements.txt`

## Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/Jal7823/laCuestesitaBackend
cd laCuestesitaBackend
```
Create a Virtual Environment:
```bash

python -m venv venv
```
Activate the Virtual Environment:

On Windows:

```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
Install Dependencies:
```bash
pip install -r requirements.txt
```
Configure the Database:

Ensure your database is set up in settings.py.

Run migrations:
```bash

python manage.py migrate
```
Create a Superuser:
```bash
python manage.py createsuperuser
```
Run the Development Server:

```bash
python manage.py runserver
```
**Usage**

Django Admin: Access the Django admin panel at http://127.0.0.1:8000/admin to manage data.
API: The API endpoints are available at the root of the development server. Check the API documentation at http://127.0.0.1:8000/api/.

**Configuration**

***INSTALLED_APPS***: Ensure the following applications are included in INSTALLED_APPS in settings.py:
```
python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.drinks',
    'apps.ingredients',
    'apps.plates',
    'apps.users',
    'apps.categories',
]
```
***Password Encryption***: Passwords are handled securely through the UserManager and the set_password method in the user model.

Contributing
If you'd like to contribute to this project, please follow these steps:

- Fork the repository.
Create a new branch for your feature (git checkout -b my-new-feature).
- Make your changes and commit them (git commit -am 'Add new feature').
- Push your changes to your fork (git push origin my-new-feature).
- Create a pull request on the original repository.
- License
- This project is licensed under the MIT License. See the LICENSE file for more details.


**Project Icons:**

🏗️ - Project Overview

🍹 - Drinks Management

🥕 - Ingredients Management

🍽️ - Plates Management

👤 - Users Management

📋 - Categories Management

