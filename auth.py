import hashlib
import getpass
import webbrowser

# Simulated user data (you'd use a proper database in real applications)
users_db = {
    "admin": "user123",
    "user01": "user123"
    # NOTE: Passwords are plain here for simplicity.
    # In production, store hashed passwords in the users_db.
}


# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to validate login
def login(username, password):
    if username in users_db:
        stored_password = users_db[username]
        # Compare hashed input password with hashed stored password
        return hash_password(password) == hash_password(stored_password)
    return False


# Function to handle login interaction
def login_process():
    print("Welcome to the Virtual Assistant! Please login.")

    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if login(username, password):
        print(f"Welcome {username}! You've successfully logged in.")

        # After successful login, open the student portal
        print("Redirecting to your student portal...")
        webbrowser.open("http://127.0.0.1:5000")  # Update with your actual portal URL
    else:
        print("Login failed. Incorrect username or password.")
