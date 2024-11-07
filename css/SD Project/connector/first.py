import getpass

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # You can replace this with your authentication logic
    if username == "admin" and password == "admin123":
        print("Login successful!")
    else:
        print("Login failed. Please try again.")

if __name__ == "__main__":
    login()
