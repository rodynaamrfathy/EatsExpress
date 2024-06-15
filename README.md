# EatsExpress

## Overview

Welcome to the EatsExpress! This project aims to create a seamless and intuitive platform for users to order food from their favorite local restaurants. Inspired by popular services like UberEats, our app provides a user-friendly interface, real-time order tracking, and reliable delivery services.

## Features

- **User Authentication:** Secure login and registration using JWT.
- **Browse Restaurants:** View detailed information and menus from local restaurants.
- **Order Management:** Add items to your cart, place orders, and track order status.
- **Payment Processing:** Payment OCD.
- **Real-Time Notifications:** Order status updates.
- **Geolocation Services:** Find nearby restaurants and delivery tracking with Google Maps.
- **Admin Dashboard:** Restaurant owners can manage their menu, view orders, and update order status.

## Architecture

![Architecture Diagram](path_to_your_architecture_diagram.png)

The architecture of this application consists of the following components:

1. **Frontend:** Built with React.js, leveraging Redux for state management and Axios for API calls.
2. **Backend:** Developed using Flask, providing RESTful APIs for frontend communication.
3. **Database:** PostgreSQL for data storage, managed via SQLAlchemy ORM.
4. **Third-Party Services:**
   - Google Maps API for geolocation services.
5. **Deployment:** Dockerized application deployed on AWS.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js and npm
- MySQL
- Docker

### Backend Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/rodynaamrfathy/EatsExpress
   ```

2. **Create Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the backend directory and add your configurations:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgresql://username:password@localhost/dbname
   STRIPE_API_KEY=your_stripe_api_key
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   ```

5. **Run Migrations:**
   ```sh
   flask db upgrade
   ```

6. **Start the Backend Server:**
   ```sh
   flask run
   ```

### Frontend Setup

1. **Navigate to Frontend Directory:**
   ```sh
   cd ../frontend
   ```

2. **Install Dependencies:**
   ```sh
   npm install
   ```

3. **Environment Variables:**
   Create a `.env` file in the frontend directory and add your configurations:
   ```env
   REACT_APP_API_URL=http://localhost:5000
   REACT_APP_GOOGLE_MAPS_API_KEY=your_google_maps_api_key
   ```

4. **Start the Frontend Server:**
   ```sh
   npm start
   ```

### Docker Setup

1. **Build and Run Docker Containers:**
   ```sh
   docker-compose up --build
   ```

## Usage

1. **Register/Login:** Create an account or log in using your credentials.
2. **Browse Restaurants:** Search for nearby restaurants using the geolocation feature.
3. **Place Order:** Add items to your cart, proceed to checkout, and make a payment.
4. **Track Order:** Receive real-time updates on your order status.
5. **Admin Dashboard:** Restaurant owners can manage their menu and orders.

## API Endpoints

### User APIs
- **POST /api/register:** Register a new user.
- **POST /api/login:** User login.
- **GET /api/user:** Get user profile.

### Restaurant APIs
- **GET /api/restaurants:** Get list of restaurants.
- **GET /api/restaurants/:id:** Get details of a specific restaurant.

### Order APIs
- **POST /api/orders:** Create a new order.
- **GET /api/orders/:id:** Get details of a specific order.
- **GET /api/orders/user/:userId:** Get orders for a specific user.

### Payment APIs
- **POST /api/payments:** Process a payment via Stripe.

For detailed API documentation, refer to the [API Reference Documentation](path_to_your_api_documentation).

## Team

- **Mohamed Yasser - Backend Developer**
  - *Responsibilities:* Developing and maintaining the backend server, creating APIs, managing the database.
- **Mohamed Essam - DevOps Engineer**
  - *Responsibilities:* Managing deployment, setting up the infrastructure, ensuring high availability.
- **Rodyna Amr - UX/UI Designer**
  - *Responsibilities:* Designing the user interface, ensuring a seamless user experience, creating mockups and prototypes.



