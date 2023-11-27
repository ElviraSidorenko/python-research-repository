# SoC: Separation of Concerns
# In computer science, separation of concerns is a design principle for separating a computer program into distinct sections such that each section addresses a separate concern.

# Separation of Concerns involves two processes: reduction of coupling and increasing cohesion. Always try to write code that is highly cohesive and has low coupling.

# There are many benefits in this approach:

# 1. Better code clarity, it's much easier to understand what's going on when everything is neatly organized.
# 2. Better code reusability. When you reuse code, it's costs less to maintain it, it's also a lot easier to extend or to fix bugs because the code is only found in one place.
# 3. Better testability. When everything is neatly isolated, testing becomes a breeze. You don't have to set up a whole testing environment, you can simply mock neighboring modules with dummy data. This way you can test your module as a black box by verifying just the output, or as a white box by verifying which methods are being run.
# 4. Faster Development. Isolating modules helps in creating/updating new features.
# 5. Organizational. When everything is neatly separated engineers can have a better development experience, by agreeing on which modules to work on and not to interfere with each other.


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None


class EmailService:
    def send_welcome_email(self, user):
        print(f"Sending welcome email to {user.email}")


# Usage example
if __name__ == "__main__":
    # Create instances
    user_manager = UserManager()
    email_service = EmailService()

    # Add a new user
    new_user = User("john_doe", "john@example.com")
    user_manager.add_user(new_user)

    # Retrieve user by username
    found_user = user_manager.get_user_by_username("john_doe")

    if found_user:
        # Send a welcome email
        email_service.send_welcome_email(found_user)
    else:
        print("User not found")

# In this example:

# The User class represents a user with a username and email.
# The UserManager class is responsible for managing users. It has methods for adding users and retrieving users by their usernames.
# The EmailService class is responsible for sending emails. It has a method for sending a welcome email to a user.
# This separation allows you to modify or extend each concern independently. For example, if you want to change how user information is stored, you can modify the UserManager class without affecting the email-sending logic in the EmailService class.
