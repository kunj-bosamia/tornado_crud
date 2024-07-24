# Tornado Async Web Application

## Overview

This project demonstrates an asynchronous single-threaded web application built using the Tornado framework. The application utilizes `SQLAlchemy[async]` and `asyncpg` for ORM, interfacing with a PostgreSQL database. The primary focus of this project is to understand the concepts of Tornado, SQLAlchemy[async], and asyncpg.

## Features

The application includes two sets of routes: user routes and post routes. 

### User Routes
- **Create User**: Add a new user to the database.
- **Get User**: Retrieve user details by ID.
- **Delete User**: Remove a user by ID.
- **Update User**: Modify user details by ID.

### Post Routes
- **Create Post**: Add a new post to the database.
- **Get Post**: Retrieve post details by ID.
- **Delete Post**: Remove a post by ID.
- **Update Post**: Modify post details by ID.

## Data Models

### User Model
- `id`: Auto-generated unique identifier.
- `name`: User's name (cannot be empty).
- `email`: User's email (cannot be empty and must be unique).

### Post Model
- `id`: Auto-generated unique identifier.
- `title`: Title of the post.
- `content`: Content of the post.
- `user_id`: Foreign key linking to the user who created the post.

## Relationships
- One user can have multiple posts.
- Each post belongs to a single user.

## Error Handling
The application includes proper error handling to ensure smooth operation and informative error messages.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
2. Navigate to the project directory:
   ```sh
   cd <project_directory>
3. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4. Install the required packages:
    ```sh
    pip install -r requirements.txt

## Running the Application Locally
To run the application locally, execute the following command:
```sh
pip install -r requirements.txt
```
## Conclusion
This project is designed to help understand the basics of building an asynchronous web application using Tornado, SQLAlchemy[async], and asyncpg. It provides a foundational structure that can be extended with more features, such as user authentication, advanced error handling, and additional routes.