# Major Project: Recommender System with AI, Django, and Vue.js

This project is a full-stack implementation of a **Recommender System** using AI techniques for product recommendation. It combines a **Django backend** with machine learning models and a **Vue.js frontend** to provide personalized recommendations for users. The project includes features such as collaborative filtering, content-based filtering, and a hybrid recommendation system.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Project Overview

This project was developed as part of the Major Project for demonstrating the integration of machine learning models with a full-stack web application. The goal of the system is to provide recommendations to users based on their interactions, reviews, and product preferences. The system uses collaborative filtering, content-based filtering, and a hybrid approach to make personalized suggestions.

## Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **Collaborative Filtering**: Recommends items based on user similarity.
- **Content-Based Filtering**: Recommends items based on the product features.
- **Hybrid Recommender**: Combines collaborative and content-based filtering techniques.
- **AI Models**: Machine learning models are trained and deployed for recommendations.
- **Real-Time Recommendations**: Provides real-time product recommendations based on user behavior.
- **API Integration**: Frontend communicates with the Django API to fetch and display recommendations.

## Tech Stack

- **Backend**: Django, Django Rest Framework (DRF)
- **Frontend**: Vue.js
- **Database**: PostgreSQL
- **Machine Learning Models**: Python (Scikit-learn, TensorFlow)
- **Authentication**: JWT (JSON Web Tokens)
- **Deployment**: Docker (optional)

## Installation

### Prerequisites

- Python 3.x
- Node.js
- PostgreSQL
- Docker (optional)

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/atabekdemurtaza/MajorProject.git
   cd MajorProject/backend

2. Create a virtual environment and install dependencies:
    
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements/dev.txt

3. Set up the database (PostgreSQL) and update the config/settings.py file with your database credentials.


4. Run migrations:

    ```bash
    python manage.py migrate

5. Start the Django server:

    ```bash
    python manage.py runserver


### Frontend Setup

1. Navigate to the frontend directory:

    ```bash
    cd ../frontend

2. Install dependencies:
    
    ```bash
    npm install

3. Start the Vue.js development server:

    ```bash
    npm run serve 

### Running with Docker

   ```bash
   docker-compose up --build
   ```

### Usage

1. Open the frontend in your browser at http://localhost:8080/.
2. Register or log in to your account.
3. Browse products, leave reviews, and get personalized recommendations.
4. The recommender system will suggest products based on your preferences and interactions.

### API Endpoints
The backend provides a set of API endpoints to interact with the recommender system.

    Authentication:
        POST /api/auth/register/ - Register a new user
        POST /api/auth/login/ - Login and obtain JWT tokens
    Recommendations:
        GET /api/products/ - Retrieve list of products
        GET /api/recommendations/ - Get product recommendations based on user behavior
    Reviews:
        POST /api/reviews/ - Submit a review for a product

Refer to the API documentation (included in the project) for more details on available endpoints.

### Testing
You can run unit tests for both the backend and frontend:

### Backend (Django)

   ```bash 
   python manage.py test
   ```

### Frontend (Vue)
   ```bash 
   npm run test
   ```

### Future Enhancements

    Improve Recommendation Accuracy: Experiment with more advanced machine learning models.
    Add Social Features: Allow users to share recommendations with friends.
    Deployment: Improve deployment pipelines with CI/CD tools like GitHub Actions.
    Mobile Compatibility: Enhance the frontend for mobile responsiveness