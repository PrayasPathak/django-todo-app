# Django Todo App

The following functionalities are provided by this `Todo` application.

- Create a new Task
- View a Task
- Update a Task
- Delete a Task

Each Task have the following attributes:

- id
- title
- description
- due date
- due time
- completed status

## Structure of Project

The project is structured as follows:

- `core/` -> contains the core configurations of the project
- `todos/` -> contains the CRUD functionality of the application
- `templates/` -> contains code for the base template for the project.

## Run the project

Follow the following steps to run the project successfully:

### 1. Create a virtual environment:

`python -m venv env`

### 2. Activate the virtual envrironment:

> On Windows: venv\scripts\activate

> on Linux/Max: source venv/Scripts/activate

### 3. Install Necessary packages

`pip install -r requirements.txt`

### 4. Run project

`python manage.py runserver`
