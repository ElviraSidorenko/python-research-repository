# Help Desk Ticketing System

This is a simple Help Desk Ticketing System implemented in Python. It is my first Python project. The system allows users to create, manage, and respond to support tickets. It is designed to streamline the process of handling support requests and providing quick resolutions.

## Getting Started

To run the Help Desk Ticketing System, follow these simple steps:

1. Make sure you have Python installed on your system. If not, you can download and install it from Python's official website.

2. Clone the file to your local machine.

3. Open a terminal or command prompt and navigate to the directory where the file is located.

4. Run the program.

## Usage

Once the program is running, you will be presented with a menu that allows you to perform various actions within the Help Desk Ticketing System.
Here are the available options:

- **Submit Ticket**: Create a new support ticket by providing the required details (ID, name, email, and description of the problem)

- **Show All Tickets**: Display a list of all created support tickets with the details.

- **Respond to Ticket**: Provide a response to an open or reopened ticket.

- **Reopen Resolved Ticket**: Reopen a previously closed ticket.

- **Display Ticket Stats**: View statistics about the number of tickets created, resolved, and open.

- **Exit**: Quit the program.

## Additional Features

- **Automatic Password Generation**: When creating a support ticket, if the description contains keywords like 'password change', the system will automatically generate a new password based on specific rules and change the status of the ticket to 'Closed'.

- **Data Validation**: The system ensures that essential data fields are not left empty, and it prevents reopening an open ticket or responding to a closed ticket. This helps maintain data integrity and prevents incomplete ticket submissions.
