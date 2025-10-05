# Library Management System 📚

This project is a full-stack application for managing a library's book catalog. It is built with a **Django REST Framework (DRF)** backend and a **React** frontend. The goal of this project was to create a robust, scalable, and secure system that demonstrates a full-stack development workflow, from database design to frontend-backend integration.

## Features 

### Backend (Django REST Framework)

* **User Authentication**: Secure endpoints for user registration and login using a token-based system.

* **Book Catalog**: Full CRUD functionality to manage book records.

* **Borrowing**: A feature that allows users to borrow books, which automatically updates the available copy count.

* **Permissions**: Protected API endpoints to ensure only authenticated users can perform actions.

* **Advanced Features**:

  * **Pagination**: The book list endpoint handles large datasets by returning paginated results.

  * **Advanced Querying**: Implemented searching and filtering by various book attributes.

  * **Custom Queries**: A dedicated endpoint to display the top 3 most borrowed books using Django's annotation features.

  * **Containerization**: The entire backend is containerized with Docker and Docker Compose.

### Frontend (React)

* **Simple Interface**: A streamlined, single-file React app that handles all core functionality.

* **Authentication Flow**: The app handles user login and registration and securely manages the authentication token.

* **Dynamic UI**: The UI reacts to user actions, displaying books, borrowed books, and most borrowed books from the API.

## Future Improvements 


* **Caching BY REDIS**:  Can use redis for future

* **Rate Limiting**: i will use token bucket algorithm to avoid user to make too many request

* **Deployment**: Deploy the containerized backend to a cloud provider and the React frontend to a static site host.

* **Admin-User Interface**: Create a separate permission layer to distinguish between regular users (who can only borrow books) and administrators (who can add, edit, and delete books).

## HOW CAN YOU GUYS RUN IT(ik you are pros already but still for formality)

To run the project locally, you will need **Docker** and **Docker Compose** installed.

1. **Clone the repository**

   ```bash
   git clone https://github.com/pixelhamza/library-management-system lbms_project

3.  Run the Backend
* Navigate to the lbms_project directory.
* Create a .env file with your database credentials.
* Run docker compose up --build to containerize and run the backend.  


4.  Run the Frontend
* In a separate terminal, navigate to the frontend directory.
* Run npm install to install dependencies.
* Run npm run dev to start the development server




