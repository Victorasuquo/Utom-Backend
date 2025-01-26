# Utom Backend API Documentation

## Overview
Utom is a workspace application where users can join via invite links. The application supports Google-based authentication, onboarding processes, and role-based access to dashboards. This documentation provides a detailed guide to the backend API built using Python Flask.

---

## Features
- Invite-only access with secure JWT tokens.
- Google-based authentication.
- Onboarding process for new users.
- Role-based access control (Admin, Workspace User, Normal User).
- MongoDB Atlas integration for storing user data.
- Secure endpoints with robust validation.

---

## Technologies Used
- **Python**: Backend development.
- **Flask**: Web framework.
- **PyJWT**: For generating and verifying JWT tokens.
- **Flask-PyMongo**: For MongoDB integration.
- **Flask-Bcrypt**: For hashing sensitive data.
- **dotenv**: For managing environment variables.
- **MongoDB Atlas**: Cloud database.

---

## Project Structure
```
Utom-Backend-API/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── onboarding.py
│   ├── dashboard.py
│   ├── utils.py
│   ├── models.py
├── run.py
├── requirements.txt
├── .env
├── README.md
```

- **`app/__init__.py`**: Initializes the Flask app and database connection.
- **`app/auth.py`**: Handles Google authentication and JWT generation.
- **`app/onboarding.py`**: Manages onboarding processes for new users.
- **`app/dashboard.py`**: Defines endpoints for accessing dashboards.
- **`app/utils.py`**: Contains helper functions (e.g., JWT validation).
- **`app/models.py`**: Defines data models and schemas for MongoDB.
- **`run.py`**: Entry point for the application.
- **`.env`**: Stores environment variables.
- **`requirements.txt`**: Lists project dependencies.

---

## Environment Variables
The application requires the following environment variables:

| Variable         | Description                                  |
|------------------|----------------------------------------------|
| `SECRET_KEY`     | Flask secret key for session security.       |
| `JWT_SECRET_KEY` | Secret key for signing JWT tokens.           |
| `MONGO_URI`      | MongoDB Atlas connection string.             |

### Example `.env` File
```plaintext
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>?retryWrites=true&w=majority
```

---

## Endpoints

### 1. Google Sign-In
**Endpoint**: `POST /auth/google-signin`

**Description**: Authenticates a user via Google and returns a JWT token.

**Request**:
```json
{
  "token": "your-google-id-token"
}
```

**Response**:
- Success:
  ```json
  {
    "access_token": "your-jwt-token"
  }
  ```
- Failure:
  ```json
  {
    "message": "Invalid Google token"
  }
  ```

---

### 2. Complete Onboarding
**Endpoint**: `POST /onboarding/complete`

**Description**: Completes the onboarding process for a new user.

**Request Headers**:
```plaintext
Authorization: Bearer <your-jwt-token>
```

**Request Body**:
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "display_name": "JohnD",
  "role": "Data Scientist"
}
```

**Response**:
```json
{
  "message": "Onboarding completed"
}
```

---

### 3. Get Dashboard
**Endpoint**: `GET /dashboard/`

**Description**: Retrieves the dashboard items based on the user role.

**Request Headers**:
```plaintext
Authorization: Bearer <your-jwt-token>
```

**Response**:
- For normal users:
  ```json
  {
    "dashboard": ["Todo", "Chats", "Screens", "Meet", "Ideas", "Files"]
  }
  ```
- For admins:
  ```json
  {
    "dashboard": ["Todo", "Chats", "Screens", "Meet", "Ideas", "Files", "Build", "Marketing"]
  }
  ```

---

## Running the Application

### Prerequisites
1. Install Python 3.8 or higher.
2. Install MongoDB Atlas and create a cluster.

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/utom-backend-api.git
   cd utom-backend-api
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your `SECRET_KEY`, `JWT_SECRET_KEY`, and `MONGO_URI`.

5. **Run the Server**:
   ```bash
   python run.py
   ```
   The server will run on `http://127.0.0.1:5000`.

---

## Testing the API with Postman

1. **Set Up Postman**:
   - Create a new collection for **Utom API**.
   - Add requests for each endpoint.

2. **Test Endpoints**:
   - **Google Sign-In**: Test authentication.
   - **Complete Onboarding**: Simulate onboarding.
   - **Get Dashboard**: Verify role-based dashboard access.

---

## Security Best Practices
1. Use strong, random keys for `SECRET_KEY` and `JWT_SECRET_KEY`.
2. Store keys securely (e.g., in environment variables).
3. Validate all incoming data to prevent injection attacks.
4. Use HTTPS in production to secure data in transit.
5. Regularly rotate JWT secret keys and invalidate old tokens.

---

## Future Improvements
1. Add email notifications for invite links.
2. Implement rate limiting to prevent abuse.
3. Enhance onboarding with profile picture uploads.
4. Integrate logging for monitoring API usage.

---

## License
This project is licensed under the MIT License.
