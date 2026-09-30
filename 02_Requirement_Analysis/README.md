# Phase 2 – Requirement Analysis

# Project Title

PocketSmart AI – Your Smart Budget & Recommendation Assistant

## 1. Introduction

The requirement analysis phase identifies the functional and non-functional requirements needed to develop PocketSmart AI.

The requirements were analyzed based on the planned functionality of the application, user needs, AI recommendation requirements, database requirements, and web application architecture.

## 2. Project Objective

The main objective of PocketSmart AI is to provide an AI-powered recommendation platform that helps users plan different activities and purchases according to their requirements and budget.

The application should allow users to:

- Create an account.
- Log in securely.
- Select a planning category.
- Enter requirements.
- Provide a budget.
- Generate recommendations.
- View previous recommendations.
- Manage their session.

## 3. Functional Requirements

### 3.1 User Registration

The system should allow new users to create an account.

Required information may include:

- Username or user identification.
- Email information where applicable.
- Password.

The registration information should be stored in the application's database.

### 3.2 User Login

Registered users should be able to log in to the application.

The system should validate the provided credentials before allowing access to authenticated functionality.

### 3.3 User Logout

The application should provide a logout mechanism so that users can safely end their session.

### 3.4 Home Interior Recommendation

Users should be able to provide requirements for home interior planning.

The system should process the requirements and generate suitable recommendations based on the available budget and user input.

### 3.5 Party Planning Recommendation

Users should be able to provide information about their party or event.

The system should generate recommendations based on the provided requirements and budget.

### 3.6 Jewelry Recommendation

Users should be able to provide jewelry-related requirements.

The system should generate recommendations based on user preferences and budget.

The application can also support an outfit image for jewelry-related recommendations.

### 3.7 Recommendation History

The application should maintain previous recommendation information so that authenticated users can access their recommendation history.

### 3.8 AI Recommendation Generation

The application should use an AI model to process user input and generate recommendation results.

### 3.9 Session Management

The application should provide mechanisms for managing authenticated user sessions.

## 4. Non-Functional Requirements

### 4.1 Performance

The application should process user requests efficiently and return recommendation results without unnecessary delay.

### 4.2 Security

User authentication information should be handled securely.

Sensitive information such as API keys should not be exposed in source code or publicly uploaded repositories.

### 4.3 Usability

The interface should be simple enough for users to enter requirements and understand the generated recommendations.

### 4.4 Reliability

The application should handle invalid inputs and unexpected situations without crashing.

### 4.5 Maintainability

The application should use a modular structure so that different components can be maintained and updated independently.

## 5. Hardware Requirements

A standard computer or laptop capable of running a Python web application is sufficient for development.

Recommended requirements include:

- Modern processor.
- At least 4 GB RAM.
- Internet connection.
- Sufficient storage for the project and dependencies.

## 6. Software Requirements

The project uses technologies including:

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Google Gemini
- HTML
- CSS
- JavaScript
- Jinja2
- Database system

## 7. External Services

The recommendation system can provide references or suggestions related to services and platforms such as:

- Amazon
- Flipkart
- IKEA
- Swiggy
- Zomato
- OYO

The availability and implementation of external services depend on the application's current implementation.

## 8. Main Application Requirements

The application should support routes and functionality related to:

- Registration
- Login
- Logout
- Token/session management
- Home recommendations
- Party recommendations
- Jewelry recommendations
- Recommendation history
- Application startup information
- Health checking

## 9. User Requirements

The user should be able to:

1. Open the application.
2. Register an account.
3. Log in.
4. Select a planning category.
5. Enter requirements.
6. Enter a budget.
7. Submit the request.
8. Receive AI-generated recommendations.
9. Review the recommendations.
10. Access previous recommendation information.

## 10. Conclusion

The requirement analysis phase defines the functional, non-functional, hardware, software, and user requirements for PocketSmart AI.

These requirements provide the basis for designing the system architecture and application interface in the project design phase.
