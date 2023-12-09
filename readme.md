# Personality Test Web App

## Overview
This Django web application allows users to take a personality test and stores the results in a MySQL database. The application provides a proof of concept where users can input Likert scale responses to three personality test questions.

## Prerequisites
- Python 3.x
- Django (install using `pip install django`)
- MySQL Database
- MySQL Workbench (optional, for database visualization)

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/personality-test-app.git
cd personality-test-app
```

### 2. Navigate to Your Project Directory

Open a new command prompt and navigate to the directory where you want to create your Django project:

```bash
cd C:\Your_path\personality_test
```

### 3. Create a Virtual Environment

If you haven't already created a virtual environment, you can do so using the following commands:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

### 4. Install Django

Install Django using `pip`:

```bash
pip install django
```

### 5. Create a Django Project

Create a new Django project. Let's call it `my_project`:

```bash
django-admin startproject my_project
```

### 6: Navigate to the Project Directory

Move into the newly created project directory:

```bash
cd my_project
```

### 7. Create a Django App

Create a Django app within your project. Let's call it `traits`:

```bash
python manage.py startapp traits
```

### 8. Configure `INSTALLED_APPS`

Open the `my_project/settings.py` file and add `'traits'` to the `INSTALLED_APPS` list:

```python
# my_project/settings.py

INSTALLED_APPS = [
    # ...
    'traits',
]
```

### 9. Define Models

Open `traits/models.py` and define your models.

### 10. Make Migrations

Run the following commands to create database migrations:

```bash
python manage.py makemigrations
```

### 11. Apply Migrations

Apply the migrations to create the database tables:

```bash
python manage.py migrate
```

### 12. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) in your browser to access the application.

## Database Visualization (Optional)

### MySQL Workbench
- Open MySQL Workbench and connect to your database server.
- Explore tables, views, and stored procedures related to the application.

## Usage
1. Open the web app in your browser.
2. Navigate to the personality test page.
3. Enter Likert scale responses for three personality test questions.
4. Submit the form to store the results in the database.
5. View the results on the result page.

## Rotating Quotes and Result Page
- The result page now includes rotating quotes about personality types.
- Visit [http://localhost:8000/personality_test/](http://localhost:8000/personality_test/) after taking the test to see the result page.

## Additional Information
- Likert Scale: A Likert scale is a psychometric scale commonly used in research to measure attitudes and opinions on a linear scale, often from "Strongly Disagree" to "Strongly Agree."

## Links
- [GitHub Repository](https://github.com/Isafarii/bigfive-app)

## License
This project is licensed under the [MIT License](LICENSE).