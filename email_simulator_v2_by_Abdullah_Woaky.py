### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declaring the class variable, with default value, for emails. 
 
    # Initialing the instance variables for emails.

    # Creating the method to change 'has_been_read' emails from False to True.
class Email():
    def __init__(self, email_address, subject_line, email_content):
        self.add = email_address
        self.sub_line = subject_line
        self.content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

    # --- Functions --- #
    # Building out the required functions for the program.

def populate_inbox():
        
        # Creating 3 sample emails and add it to the Inbox list. 
        # inbox.append()?
    email1 = Email("waki2000@hotmail.com", "subject line 1", "content of email1 email")
    email2 = Email("sarah2222@hotmail.com", "subject line 2", "content2 of email2 email")
    email3 = Email("david3333@hotmail.com", "subject line 3", "content3 of email3 email")
    #email = (email1+ email2+ email3)
    inbox.extend([email1,email2,email3])
 

def list_emails():
        
        # Creating a function which prints the email’s subject_line, along with a corresponding number.
    for i, item in enumerate(inbox,1):
        print(f" Index: {i}, Subject:  {item.sub_line}!")
        print("~"*50)
    

def read_email(index):

        # Function which displays a selected email. 
        # Once displayed, call the class method to set its 'has_been_read' variable to True.
        #run for loop for specific list of selected email based on the enumerate number selection
        #modify the status to has been read to true
    selected_email = inbox[index]
    print("~"*50)
    print(f"You have select index {index+1} : !Email address:! {selected_email.add} !Subject:! {selected_email.sub_line} !Content:! {selected_email.content} \n")
    print("*"*50)
    selected_email.mark_as_read() # mark the email that has been read just now
    print(f"The email address {selected_email.add} now marked as read")
    print("~"*50)
    
    
# --- Email Program --- #

# Calling the function to populate the Inbox for further use in program.

populate_inbox()

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # Display the list of emails and ask the user to select the index
        list_emails()
        print("~"*50)
        index = int(input(" ***Enter the index of the email you wish to read(1,2,3)?*** : "))
        print("~"*50)
        index = index-1 # deduct -1 from user input to match the true list index
        read_email(index) # read the email and mark it as read.
        print("~"*50)
        
    elif user_choice == 2:
        # Declaring an email list for unread emails.
        unread_emails = []
        for item in inbox:
           if not item.has_been_read : # check which email has not been read
               unread_emails.append(item) # append them to the unread emails list
        if unread_emails:
            print(f" ***Unread emails are:*** \n")
            for email in unread_emails:
                print("~"*50)
                print(email.sub_line) # now read through the unread email list and print the subject line
            print("~"*50)
        else:
            print("no unread emails")     
            
    elif user_choice == 3:
        # add logic here to quit appplication
        print("~"*50)
        print("Goodbye for now")
        print("~"*50)
        break

    else:
        print("~"*50)
        print("Oops - incorrect input.")
        print("~"*50)

