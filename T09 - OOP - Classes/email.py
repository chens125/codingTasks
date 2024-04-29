'''
Purpose: Simulate a basic email management system allowing users to read emails, mark them as read, and view unread emails.

1. Define an Email class:
    - Attributes: email address, subject line, email content, and whether it has been read.
    - Method: mark_as_read() to update the read status.

2. Define functions:
    - populate_inbox(): Creates and returns a list of email objects.
    - list_emails(inbox): Prints the list of emails in the inbox.
    - read_email(inbox): Displays a selected email, marks it as read, and prints its content.
    - read_unread_emails(inbox): Lists and displays unread emails.
    - quit_application(): Prints a quit message and exits the program.

3. Main program:
    - Populate the inbox.
    - Enter a loop to display a menu and handle user input.
    - Display options to read an email, view unread emails, or quit.
    - Call corresponding functions based on user input.
'''

#Step 1#
class Email:

    #constructer method
    def __init__(self, email_address,subject_line,email_content): 
        self.email_address=email_address
        self.subject_line=subject_line
        self.email_content=email_content
        self.has_been_read=False # Defaults

    #class methods
    def mark_as_read(self):
        self.has_been_read=True
           


# Step 2 #
def populate_inbox():
    inbox = []
    inbox.append(Email("gmail.com", "Welcome to HyperionDev!", "Hi gmail"))
    inbox.append(Email("hotmail.com", "Great work on the bootcamp!", "Hi hotmail"))
    inbox.append(Email("qqmail.com", "Your excellent marks!", "Hi qqmail"))
    return inbox

def list_emails(inbox):
    print('''
...........................................................
    Check the email list below\n''')
    for index, email in enumerate(inbox):
        print(f"{index} - {email.subject_line}")

def read_email(inbox):
    # Select and read the chosen email#
    list_emails(inbox)
    index = int(input("\nEnter the index of the email you want to read: "))
   
    email = inbox[index]
    print(f"\nFrom: {email.email_address}\nSubject: {email.subject_line}\nContent:{email.email_content}")

    # Mark as read#
    email.mark_as_read()
    print("\n** Email marked as read. **\n")

def read_unread_emails(inbox):
    print('''
    .............................................................
        Check the unread email list below\n''')
    for index, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{index} - {email.subject_line}")

def quit_application():
    print("Quitting application.\n")
    quit()


# Step 3#

# Call the function to populate the Inbox for further use in your program.
# Fill in the logic for the various menu operations.
inbox=populate_inbox()

while True:
    user_choice = int(input('''\n
................................................................
    Would you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: 
\n'''))
       
    if user_choice == 1:
        read_email(inbox)
        
    elif user_choice == 2:
        read_unread_emails(inbox)
            
    elif user_choice == 3:
        quit_application()

    else:
        print("Oops - incorrect input.\n")