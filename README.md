# Football Team Formation API


A simple CRUD project built for a test at [Scopic Software](https://scopicsoftware.com) according to their requirements.
This project uses Python, Django, Django Rest Framework for backend and SQLite as database to be able to run it anywhere.

The initial project was created by Scopic, hence the project structure was already defined.
The project was maintained in a platform provided by them named Codeaid.

## Features
- **Player CRUD Operations**: Create, read, update, and delete player data with skills
- **Player Listing**: Retrieve all players with their skill information
- **Team Formation**: Intelligent team formation algorithm based on player skills and requirements


## Implementation Details
- **Backend**: Django REST Framework for RESTful API endpoints
- **Database**: SQLite for easy deployment anywhere
- **Architecture**: Modular API structure with separate handlers for player and team operations
- **Data Models**: 
  - Player model with associated skills
  - PlayerSkill model for managing player capabilities
  - Comprehensive serializers for data validation and transformation
## Requirements
- Python 3.x
- Django 5.x

## Setup Instructions

First, clone this repository to your local machine
```bash
git clone https://github.com/Ishtiaque-h/football-team-api.git
```

Create a virtual environment and activate it
```bash
python -m venv football_env
```

For Windows
```bash
football_env\Scripts\activate
```

For Linux/macOS
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

Run migrations
```bash
python manage.py migrate
```

Finally, run the development server
```bash
python manage.py runserver
```

## API Endpoints

- `GET /api/player` - List all players
- `POST /api/player` - Create a player
- `PUT /api/player/{id}` - Update a player
- `DELETE /api/player/{id}` - Delete a player
- `POST /api/team/process` - Build a team from requested skills

## Running Tests

Run all tests:
```bash
python manage.py test
```

Test files are in `my_app/tests`.

If XML test runner is enabled in settings, XML reports are generated in `test_output`.