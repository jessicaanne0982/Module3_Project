import json
import re

def add_contact(contact_list):
    while True:
        try:
            new_email = input("\nEnter email address: ")
            if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}", new_email):
                found = False
                for contact in contact_list:
                    if new_email in contact_list:      
                        print("\nThis contact already exists in the Contact List.")
                        found = True
                        break
                else:
                    print("\nThat email was not found. Add contact now:\n")
                    name = input("Enter name: ")
                    phone_number = input("Enter phone number (xxx-xxx-xxxx): ")
                    if not re.search(r"\d{3}-\d{3}-\d{4}", phone_number):
                        print("Invalid phone number format. Try again.")
                        break
                    birthday = input("Enter birthday (xx/xx/xxxx): ")
                    if not re.search(r"\d{2}\/\d{2}\/\d{4}", birthday):
                        print("Invalid birthday format. Try again.")
                        break
                    contact_list.append({new_email : {"Name" : name, "Phone Number" : phone_number, "Birthday": birthday}})
                    print(f"\n{name} has been added to the contact list with an email address of {new_email}.")
            else:
                print("Invalid email format.  Please try again.")
                break
        except ValueError:
            print("\nInvalid entry.  Please try again.")
        continue_input = input("\nWould you like to add another contact? (yes/no) ")
        if continue_input != 'yes':
            break

def edit_contact(contact_list):  # ADD ERROR CATCHING... REGEX FOR PHONE AND BIRTHDAY SYNTAX
    while True:
        contact_to_edit = input("\nEnter the email of the contact to edit: ")
        if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}", contact_to_edit):
            found = False
            for contact in contact_list:
                if contact_to_edit in contact:      
                    option = input("\nChoose option to edit: \n[1]Name, [2]Phone Number, [3]Birthday ")
                    if option == "1":
                        name_change = input("\nEnter the name change: ")
                        contact[contact_to_edit]["Name"] = name_change 
                        print(f"\nContact name has been updated to {name_change}")
                        found = True
                        break
                    elif option == "2":
                        number_change = input("\nEnter the phone number change (xxx-xxx-xxxx): ")
                        if not re.search(r"\d{3}-\d{3}-\d{4}", number_change):
                            print("Invalid phone number format. Try again.")
                            break
                        contact[contact_to_edit]["Phone Number"] = number_change
                        print(f"\nContact phone number has been updated to {number_change}")
                        found = True
                        break
                    elif option == "3":
                        birthday_change = input("\nEnter the birthday change (xx/xx/xxxx): ")
                        if not re.search(r"\d{2}\/\d{2}\/\d{4}", birthday_change):
                            print("Invalid birthday format. Try again.")
                            break
                        contact[contact_to_edit]["Birthday"] = birthday_change
                        print(f"\nContact birthday has been updated to {birthday_change}")
                        found = True
                        break
                    else:
                        print("\nInvalid entry. Please enter a number 1 to 3.")
            else:
                print(f"\nThe contact information for email: {contact_to_edit} was not found.")
        else:
            print("Invalid email format.  Please try again.")
        continue_input = input("\nWould you like to edit another contact? (yes/no) ")
        if continue_input != 'yes':
            break

def delete_contact(contact_list): 
    while True:   
        contact_to_delete = input("\nEnter the email of the contact to delete: ")
        if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}", contact_to_delete):
            found = False
            for index, contact in enumerate(contact_list):
                if contact_to_delete in contact:       
                    del contact_list[index]  
                    print(f"\nThe contact information for {contact_to_delete} has been deleted.")
                    found = True
                    break
            else:
                print(f"\n{contact_to_delete} was not found in the contact list.")
        else:
            print("Invalid email format.  Please try again.")
        continue_input = input("\nWould you like to delete another contact? (yes/no) ")
        if continue_input != 'yes':
            break

def search_contact(contact_list): 
    while True: 
        email_to_search = input("\nEnter the email to search: ")
        if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}", email_to_search):
            found = False
            for contact in contact_list:
                if email_to_search in contact.keys():   
                    print(f"\nName: {contact[email_to_search]["Name"]} \nEmail Address: {list(contact.keys())[0]} \
                        \nPhone Number: {contact[email_to_search]["Phone Number"]} \nBirthday: {contact[email_to_search]["Birthday"]}"
                    )
                    found = True
                    break
            else:
                print(f"\n{email_to_search} was not found in the contact list")
        else:
            print("Invalid email format.  Please try again.")
        continue_input = input("\nWould you like to search for another contact? (yes/no) ")
        if continue_input != 'yes':
            break
 
def display_all_contacts(contact_list): 
    for contact in contact_list:
        print(f"\n{contact}")

def export_contacts_to_file(filename, contact_list):  
    try:
        export_file = open('Contact_List.txt', 'w')
        for contact in contact_list:
            json.dump(contact, export_file)
            export_file.write("\n")    
        print(f"\nContact List has been exported to {filename}")
    except FileNotFoundError:
        print(f"{filename} not found.")

def import_contacts_from_file(filename):
    filename = 'Contact_List.txt'
    try:
        contact_list = []
        for line in open('Contact_list.txt', 'r'):
            contact_list.append(json.loads(line))
            print(line)
    except FileNotFoundError:
        print(f"file not found.")
   
contact_list= []

print("\nWelcome to the User Management System!")

def main():
    contact_list= []
    while True:
        print("\nMENU:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file *BONUS*")
        print("8. Quit")
        user_choice = input("Enter an option from above: ")

        if user_choice == '1':
            add_contact(contact_list)
        elif user_choice == '2':
            edit_contact(contact_list)
        elif user_choice == '3':
            delete_contact(contact_list)
        elif user_choice == '4':
            search_contact(contact_list)
        elif user_choice == '5':
            display_all_contacts(contact_list)
        elif user_choice == '6':
            export_contacts_to_file('Contact_List.txt', contact_list)
        elif user_choice == '7':
            import_contacts_from_file('Contact_List.txt')
        elif user_choice == '8':
            print("Thank you for using the Contact Management System.")
            break
        else:
            print("Invalid choice!  Please choose again: ")

if  __name__ == "__main__":
    main()  
