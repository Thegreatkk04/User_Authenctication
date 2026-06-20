# User_Authenctication
Here We will do authentication using email verification
# User Authentication App

A secure user authentication application built using **Streamlit** and **Supabase Authentication**. The application allows users to create accounts, log in

## Features

* User Registration (Sign Up)
* User Login
* Secure Authentication with Supabase
* Email Verification Support
* Session Management
* Logout Functionality
* Streamlit-based User Interface

## Tech Stack

* Python
* Streamlit
* Supabase Authentication
* PostgreSQL (Managed by Supabase)

## Project Structure

```text
.
├── main.py
├── requirements.txt
├── README.md

```



## Application Workflow

### Sign Up

* User enters email and password.
* Account is created using Supabase Authentication.
* Verification email is sent (if enabled).

### Login

* User enters registered credentials.
* Supabase verifies credentials.
* User gains access to protected content.

### Logout

* User session is terminated.
* User is redirected to the login screen.

## Live Demo

https://user-session.streamlit.app/

## Security Features

* Passwords securely handled by Supabase
* Email verification support
* Session-based authentication
* Secure environment variable management
* No credentials stored in source code

## Future Enhancements

* Password Reset
* Google Authentication
* GitHub Authentication
* Profile Management
* User Roles and Permissions
* Multi-Factor Authentication (MFA)
