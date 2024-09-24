# Football Team Formation API


A simple CRUD project built for a test at Scopic Software according to their requirements.
This project uses Python, Django, Django Rest Framework for backend and SQLite as database to be able to run it anywhere.
The initial project was created by them, hence the project structure was already defined.
The project was maintained in a platform provided by them named Codeaid.

## Features
- Save, Update, Delete Player Data
- List of All Players
- Form a Team according to Requirement


## Requirements
- Python 3.x
- Django 4.x or later

## Setup Instructions

### 1. Clone the repository
First, clone this repository to your local machine
```bash
git clone https://github.com/HqShiblu/Football-Team-Api.git
```

Create a virtual environment and activate it
```bash
python -m venv football_env
```

For Windows
```bash
source football_env\Scripts\activate
```

For Linux
```bash
source football_env\bin\activate
```

Now, go to project directory
```bash
cd football-team-api
```

Install the required packages

```bash
pip install -r requirements.txt
```

Finally, run the development server
```bash
python manage.py runserver
```

You will find the test cases in _my_app/tests_ folder.