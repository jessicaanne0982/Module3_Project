Contact Management System

Description:
Using Python, the Contact Management System allows a user to fully manage a list of contacts and their pertinent information.
Filtering by a contact's email address, users are able to perform a number of different operations including editing the 
contact information, deleting contacts, searching for a specific contact's information, displaying all contacts, exporting 
contacts to a .txt file, and importing contact information from a .txt file.

How to Run:
The program can easily be run in a computer's Terminal window.

Usage:
When the user initiates the program, they are greeted with a Welcome message and the following menu of options to choose from.

1. Add a new contact - This option first looks to see if the entered email address already exists in the list.  If not,
    it prompts the user to enter the contact name, phone number, and birthday, ensuring each entry is typed in the correct
    format and then added to the list.
2. Edit an existing contact - Editing the contact is just as it seems.  Beginning with a check of the contact's email address,
    it asks the user if they would like to change the name, phone number, or birthday.  Depending on the number the user enters,
    the program will run a check to ensure all entries are the correct format and will then update the contact information in the 
    list.
3. Delete a contact -  This option takes the contact's email address and deletes all information associated with it.
4. Search for a contact - This options allows the user to enter a specific email address and view only the information associated
    with it.
5. Display all contacts - When chosen, option 5 presents the user with the full list of contacts and all information connected to 
    them.
6. Export contacts to a file - Option 6 exports all contact information found within the list of contacts to a file named 
    'Contact_list.txt'. 
7. Import contacts from a file - This choice will take all the contacts present in the 'Contact_List.txt' file, import them, and 
    print them to the terminal window.
8. Quit - Option 8 quits the program.


