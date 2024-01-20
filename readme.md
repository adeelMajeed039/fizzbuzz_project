# 🎉 FizzBuzz API Project 🎉

## 📚 Overview
Welcome to the FizzBuzz API Project! This is a Django-based web application that implements a FizzBuzz API using the powerful Django Rest Framework. Our API allows you to create, list, and retrieve FizzBuzz objects, each with a unique ID, user agent, creation date, and a custom message.

## ✨ Features
Here's what you can do with our API:

- 📝 Create a new FizzBuzz object with a POST request.
- 📚 List all FizzBuzz objects with a GET request.
- 🔍 Retrieve a specific FizzBuzz object by its ID with a GET request.

## 🚀 Installation
Ready to set up and run the FizzBuzz API on your local machine? Just follow these steps:

1. **Clone the Repository**
```bash
git clone [repository-url]
cd fizzbuzz_project
```

2. **Install Required Packages**
Make sure you have Python installed on your system. Then, install the required packages:
```bash
pip install -r requirements.txt
```

3. **Database Migrations**
Run the following commands to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```


4. **Running the Server**
Start the Django development server:
```bash
python manage.py runserver
```


## 🛠 Usage
The API endpoints are as follows:

- **List FizzBuzzes**: `GET /fizzbuzz`
- **Retrieve a FizzBuzz**: `GET /fizzbuzz/{fizzbuzz_id}`
- **Create a FizzBuzz**: `POST /fizzbuzz` with a JSON body containing a `message`.

## 🧪 Testing
To run the automated test suite, execute the following command:
python manage.py test fizzbuzz_app