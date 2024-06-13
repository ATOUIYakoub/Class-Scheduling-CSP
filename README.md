# Backend Class Scheduling CSP

This project is a Django-based backend for a class scheduling system. It employs Constraint Satisfaction Problem (CSP) techniques, specifically AC-3 (Arc Consistency Algorithm #3) and backtracking, to generate feasible timetables for classes.

## Table of Contents
- [Backend Setup](#Backend-Setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [Timetable Scheduling](#timetable-scheduling)
- [Frontend Setup](#frontend-setup)
- [Contributing](#contributing)

## Backend Setup

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/ATOUIYakoub/Backend-class-scheduling-CSP.git
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate   # On Windows use `.\env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
    **Note**: If the migrations do not work, you can comment out the contents of `csp_utils.py` and related references in `views.py`. After running the migration commands, uncomment the previously commented lines.

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Configuration

Ensure that you configure your database and other settings in the `settings.py` file as required. The default configuration uses SQLite for simplicity.

## Usage

1. Access the Django admin interface at `http://127.0.0.1:8000/admin` and log in using the superuser credentials created earlier.
2. Use the admin interface to input data about classrooms, courses, instructors, and timeslots.
3. The timetable scheduling algorithm can be triggered via the provided endpoints or by implementing custom views.
4. To test with Swagger, access the API documentation at `http://127.0.0.1:8000/api/schema/docs`.

## Timetable Scheduling

The timetable scheduling feature is implemented using CSP techniques. Here's a brief overview of how AC-3 and backtracking are used:

### AC-3 (Arc Consistency Algorithm #3)
AC-3 is used to reduce the search space before applying the backtracking algorithm. It works by enforcing consistency between variable pairs (arcs). If any variable's domain is emptied, the problem is unsolvable under the current constraints.

### Backtracking
After the initial reduction by AC-3, backtracking is employed to search for solutions. The backtracking algorithm recursively assigns values to variables while ensuring that constraints are satisfied. If a conflict arises, it backtracks to the previous step and tries a different assignment.

### Implementation
- **csp_utils.py**: Contains utility functions to support the CSP solver.

To execute the timetable scheduling:
1. Ensure that you have populated the database with the necessary data (classrooms, courses, instructors, and timeslots).
2. Use the provided management commands or views to trigger the scheduling process.

## Frontend Setup

The frontend for this project is built using React and is located in the `Front-end` folder. Follow these steps to set up and run the frontend:

1. Navigate to the `Front-end` directory:
    ```sh
    cd front-end
    ```

2. Install the required dependencies:
    ```sh
    npm install
    ```

3. Build the React application:
    ```sh
    npm run build
    ```

4. Start the development server:
    ```sh
    npm start
    ```

5. Access the React application at `http://localhost:5000`.

Ensure that your backend server is running concurrently to enable full functionality.

## Screenshots

Here are some screenshots of the application:

### Timetable For Teacher
![Timetable View](screenshots/timetable_view.png)

### Timetable For Groups
![Scheduling Algorithm](screenshots/scheduling_algorithm.png)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.
