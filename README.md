﻿# To-Do App with CRUD Functionality

Project Overview

This project is a simple CRUD (Create, Read, Update, Delete) application designed as a learning experience for building a full-stack app. It consists of:

Login Page: Allows users to log in with their credentials.

To-Do List Page: Enables users to manage their tasks with CRUD operations.


Technologies Used

Frontend:

React.js: Framework for building the user interface.

Material UI: For designing responsive and modern components.

React Router: For seamless page navigation.


Backend:

Flask API: Lightweight Python framework for handling backend logic and API requests.


Database:

SQLite: Lightweight relational database for storing user and task data.



---

How to Run the Project

Prerequisites:

1. Install Node.js for running the React frontend.


2. Install Python (3.8 or above) for the backend.


3. Install pip (Python package manager) for Python dependencies.




---

Frontend Setup

1. Clone the repository:

git clone (https://github.com/tinyfroggy/auth-todo-list)
cd frontend


2. Install dependencies:

npm install


3. Run the frontend server:

npm start

The app will run at http://localhost:3000.




---

Backend Setup

1. Navigate to the backend folder:

cd backend


2. Install dependencies:

pip install -r requirements.txt


3. Run the Flask API server:

python app.py

The API will run at http://localhost:5000.




---

Connecting the Frontend and Backend

Make sure the backend URL (http://localhost:5000) is properly configured in the React app



---

Testing the Application

1. Open the frontend in your browser at http://localhost:3000.


2. Use the login page to enter credentials.


3. Manage tasks (add, view, edit, delete) on the To-Do List page.




---

Future Enhancements

Add authentication with JWT.

Use a more robust database (e.g., PostgreSQL).

Deploy the app on cloud platforms like AWS or Heroku.


Let me know if you'd like adjustments or more details!
