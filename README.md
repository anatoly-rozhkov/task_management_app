# Task Management Django Backend

This is the backend API for the Task Management application, built with Django.

## Features

- REST API for managing tasks
- Swagger UI available for API documentation

## Getting Started

1. Copy the example environment file:

   ```bash
   cp .env-example .env

2. Start the application with:
    ```bash
    make up
    ```
   
3. Access the API documentation (Swagger UI) at:
http://0.0.0.0:8080/api/schema/tm/swagger/


4. Access the Admin Panel
Open your browser and go to:
http://localhost:8080/admin/

Use the following credentials to log in:

Username: admin@admin.com

Password: string

## Notes
 - Make sure to configure your .env file with the correct settings before running.
 - The backend runs on port 8080 by default.
 - IMPORTANT: start backend part before frontend part

## Frontend 
https://github.com/anatoly-rozhkov/Project-Management-App