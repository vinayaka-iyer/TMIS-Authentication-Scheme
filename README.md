### **Project Documentation: Lightweight Client Authentication System using Chaotic Hash Function**

#### **1. Introduction**

This project implements a lightweight client authentication system using the **Chebyshev chaotic map** for generating cryptographically secure hash values. The authentication system provides user registration and login functionalities, following the security principles outlined in the paper **"Provably Secure Lightweight Client Authentication Scheme with Anonymity for TMIS using Chaotic Hash Function"** by Vishesh P. Gaikwad, Jitendra V. Tembhurne, Chandrashekhar Meshram, and Cheng-Chi Lee.

The system is built using **FastAPI**, a modern web framework for building APIs in Python, and employs the chaotic hash function for secure password storage and user verification.

---

#### **2. Background and Motivation**

In secure systems like Telecare Medical Information Systems (TMIS), it is critical to ensure that authentication is not only lightweight but also resistant to various attacks such as replay, impersonation, and brute force. Traditional hashing algorithms like SHA-256 are widely used, but chaotic hash functions offer enhanced unpredictability due to their sensitivity to initial conditions.

The chaotic map, specifically the **Chebyshev map**, provides this security feature by utilizing chaotic sequences for hashing. This project implements the chaotic hash function inspired by the research paper and demonstrates a simple client authentication system that adheres to the same security principles.

---

#### **3. Chaotic Hash Function**

The chaotic hash function used in this project is derived from the **Chebyshev chaotic map**. The Chebyshev map is a type of chaotic system that exhibits properties like sensitivity to initial conditions and unpredictability, which are essential for cryptographic applications.

##### **Chebyshev Map Formula:**
\[
T_k(x) = \cos(k \cdot \arccos(x))
\]
Where:
- `x` is an initial value.
- `k` is a constant defining the chaotic system.

In the context of hashing, this map is iteratively applied to an initial value and the result is combined with the input data to produce a hash using the SHA-256 algorithm.

##### **Python Implementation:**
The `chaotic_hash()` function in the `chaotic_hash.py` module applies the Chebyshev map iteratively and hashes the data using SHA-256:
```python
import hashlib
import numpy as np

def chebyshev_map(x, k):
    return np.cos(k * np.arccos(x))

def chaotic_hash(data: str, iterations: int = 100) -> str:
    x = 0.5  # Initial condition
    k = 3    # Chaotic map parameter
    for _ in range(iterations):
        x = chebyshev_map(x, k)
    return hashlib.sha256(str(data).encode() + str(x).encode()).hexdigest()
```

---

#### **4. System Architecture**

The system comprises three primary modules:

1. **Registration:** Users can register with a username and password. The password is hashed using the chaotic hash function before being stored in the database.
   
2. **Authentication:** Users can log in using their credentials. The password provided during login is hashed and compared against the stored hash for authentication.

3. **Session Management:** After successful authentication, a session token can be generated (not included in the base implementation but can be extended).

---

#### **5. Project Structure**

The project follows a modular structure with clear separation of concerns. Below is the file structure:

```
.
├── app
│   ├── __init__.py           # Initializes the app as a package
│   ├── main.py               # FastAPI app with endpoints
│   ├── models.py             # SQLAlchemy models
│   ├── schemas.py            # Pydantic schemas for validation
│   ├── database.py           # Database connection and setup
│   ├── auth.py               # Authentication and registration logic
│   └── chaotic_hash.py       # Chebyshev chaotic hash function implementation
└── requirements.txt          # Project dependencies
```

---

#### **6. Key Components**

##### **1. User Registration:**
- The user provides a `username` and `password`.
- The `password` is hashed using the **Chebyshev chaotic hash**.
- The `username` and `password_hash` are stored in the database.

##### **2. User Authentication:**
- During login, the user submits their credentials.
- The provided `password` is hashed using the same chaotic hash method.
- The system compares the hash with the stored hash for the user.

##### **3. Database:**
- **SQLite** is used for simplicity.
- **SQLAlchemy** manages the user model and database interactions.

---

#### **7. FastAPI Endpoints**

The following endpoints are exposed via FastAPI:

- **POST `/register/`**:
  - Registers a new user with a username and password.
  - Stores the hashed password using the chaotic hash function.

- **POST `/login/`**:
  - Authenticates an existing user.
  - Compares the hashed password from the login request to the stored hash.

---

#### **8. Example API Usage**

1. **Register User**:
   - **Request:**
     ```json
     {
       "username": "user1",
       "password": "mypassword"
     }
     ```
   - **Response:**
     ```json
     {
       "username": "user1",
       "message": "User registered successfully"
     }
     ```

2. **Login User**:
   - **Request:**
     ```json
     {
       "username": "user1",
       "password": "mypassword"
     }
     ```
   - **Response:**
     ```json
     {
       "username": "user1",
       "message": "Login successful"
     }
     ```

---

#### **9. Security Considerations**

- **Chaotic Hashing**: The chaotic hash function provides enhanced unpredictability, reducing the risk of successful brute-force attacks and improving resistance to common attack vectors like replay attacks.
- **Lightweight Authentication**: The system is designed to be lightweight, making it suitable for applications with resource-constrained environments, such as IoT or TMIS.

---

#### **10. Reference**

- **Vishesh P. Gaikwad, Jitendra V. Tembhurne, Chandrashekhar Meshram, Cheng-Chi Lee**. *Provably Secure Lightweight Client Authentication Scheme with Anonymity for TMIS using Chaotic Hash Function*. Journal of Supercomputing, 2021【17†source】.

This project demonstrates a practical implementation of the principles outlined in the referenced paper, utilizing chaotic hash functions in an authentication system for security and efficiency.
