class Ticket:
    counter = 2001
    tickets = []

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.counter
        Ticket.counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.tickets.append(self)

    @staticmethod
    def validate_input(prompt, error_message):
        user_input = input(prompt)
        while not user_input:
            print(error_message)
            user_input = input(prompt)
        return user_input

    @classmethod
    def create_ticket(cls, staff_id, creator_name, contact_email, description):
        password_change_options = ['password change', 'pasword change', 'passwordchange', 'paswordchange',
                                   'change password', 'changepassword', 'change pasword', 'changepasword']
        ticket = cls(staff_id, creator_name, contact_email, description)
        if description.lower() in password_change_options:
            ticket.generate_password()
        else:
            print(f"\nTicket {ticket.ticket_number} created successfully!")

    @classmethod
    def submit_ticket(cls):
        affirmative_options = ['y', 'yes']
        negative_options = ['n', 'no']
        submit = 'y'
        while submit.lower() in affirmative_options:
            staff_id = cls.validate_input(
                "\nEnter Staff ID: ", "Staff ID cannot be empty. Please enter a valid value.")

            creator_name = cls.validate_input(
                "Enter Ticket Creator Name: ", "Ticket Creator Name cannot be empty. Please enter a valid value.")

            contact_email = cls.validate_input(
                "Enter Contact Email: ", "Contact Email cannot be empty. Please enter a valid value.")

            description = cls.validate_input(
                "If you require a new password - type 'Password change'.\nEnter Description of the Problem: ", "Description cannot be empty. Please enter a valid value.")

            cls.create_ticket(staff_id, creator_name,
                              contact_email, description)
            submit = input(
                '\nWould you like to submit another ticket? Y/N ').lower()
            while (submit not in negative_options) and (submit not in affirmative_options):
                submit = input(
                    '\nInvalid input. Please enter a valid response. Y/N ')

    def generate_password(self):
        self.response = f"\nNew password generated: {
            self.staff_id[:2] + self.creator_name[:3]}"
        self.status = 'Closed'
        print(self.response)
        print(f"Ticket {self.ticket_number} is now Closed.")

    @classmethod
    def reopen_ticket(cls, ticket_number):
        for ticket in cls.tickets:
            if str(ticket.ticket_number) == ticket_number:
                if ticket.status == 'Closed':
                    ticket.status = "Reopened"
                    print(f'\nTicket {ticket.ticket_number} has been reopened')
                    return
                else:
                    print('\nTicket is alredy open')
                    return
        print('\nTicket not found')

    @classmethod
    def provide_response(cls, ticket_number):

        for ticket in cls.tickets:
            if str(ticket.ticket_number) == ticket_number:
                if ticket.status == 'Open' or ticket.status == 'Reopened':
                    response = input('Enter response to the Ticket: ')
                    ticket.response = response
                    ticket.status = 'Closed'
                    print(
                        f"\nTicket {ticket.ticket_number} has been closed.")
                    return
                else:
                    print("\nTicket has been closed. Try to reopen first.")
                    return
        print('\nTicket not found')

    @classmethod
    def get_ticket_stats(cls):
        total_tickets = len(cls.tickets)
        resolved_tickets = sum(
            1 for ticket in cls.tickets if ticket.status == "Closed")
        open_tickets = total_tickets - resolved_tickets
        print(f'\nTickets Created: {total_tickets}')
        print(f'Tickets Resolved: {resolved_tickets}')
        print(f'Tickets To Solve: {open_tickets}')

    @classmethod
    def display_tickets(cls):
        if len(cls.tickets) > 0:
            for ticket in cls.tickets:
                print(f"\nTicket Number: {ticket.ticket_number}")
                print(f"Ticket Creator: {ticket.creator_name}")
                print(f"Staff ID: {ticket.staff_id}")
                print(f"Email Address: {ticket.contact_email}")
                print(f"Description: {ticket.description}")
                print(f"Response: {ticket.response}")
                print(f"Ticket Status: {ticket.status}")
        else:
            print('\nNo tickets to show')


class Main:

    def action_selection(selection):

        if selection == '1':
            Ticket.submit_ticket()
        elif selection == '2':
            Ticket.display_tickets()
        elif selection == '3':
            ticket_number = input("\nEnter Ticket Number to Respond: ")
            Ticket.provide_response(ticket_number)
        elif selection == '4':
            ticket_number = input("\nEnter Ticket Number to Reopen: ")
            Ticket.reopen_ticket(ticket_number)
        elif selection == '5':
            Ticket.get_ticket_stats()
        else:
            print("\nInvalid choice. Please try again.")

    def main():
        while True:
            print("\nHelp Desk Ticketing System:")
            print("0: Exit")
            print("1: Submit Ticket")
            print("2: Show All Tickets")
            print("3: Respond to Ticket")
            print("4: Reopen Resolved Ticket")
            print("5: Display Ticket Stats")

            choice = input("Enter your choice: ")
            if choice == '0':
                break
            else:
                Main.action_selection(choice)


if __name__ == "__main__":
    Main.main()
