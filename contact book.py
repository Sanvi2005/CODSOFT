import json
import os
import re

# A file for storing contacts:
CON_FILE = "contacts.json"

# Function to load contacts from JSON file:
def load_contacts():
    if os.path.exists(CON_FILE):
        with open(CON_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save contacts to JSON file:
def save_contacts(contacts):
    with open(CON_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Function to display a welcome message:
def display_welcome():
    try:
        cons_width = os.get_terminal_size().columns
    except OSError:
        cons_width = 80  # Default width if terminal size can't be determined
    welcome_msg = "--- Welcome to the Smart Contact Book ---"
    instruction_msg = "Store your contacts easily and efficiently."
    print("\n" + welcome_msg.center(cons_width))
    print(instruction_msg.center(cons_width) + "\n")

# Function to check for duplicates
def contact_exists(contacts, phone, email):
    return [contact for contact in contacts if contact["phone"] == phone or contact["email"] == email]

# Function to validate phone numbers
def is_valid_phone(phone):
    return re.match(r"^\+?1?\d{9,15}$", phone) is not None  # Example pattern for international format

# Function to validate emails
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None  # Simple regex for email validation

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    while not is_valid_phone(phone):
        print("Invalid phone number. Please enter a valid phone number.")
        phone = input("Enter phone number: ")
    
    email = input("Enter email: ")
    while not is_valid_email(email):
        print("Invalid email address. Please enter a valid email.")
        email = input("Enter email: ")
    
    address = input("Enter address: ")

    # Check for duplicate contact
    existing_contacts = contact_exists(contacts, phone, email)
    
    if existing_contacts:
        print("A contact with the same phone number or email already exists.")
        for contact in existing_contacts:
            print(f" - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        replace = input("Do you want to replace the existing contact(s)? (yes/no): ").strip().lower()
        if replace != 'yes':
            print("Contact not added.")
            return
        else:
            # Replace existing contacts with the new one
            for contact in existing_contacts:
                contacts.remove(contact)
            print("Existing contact(s) replaced with the new contact.")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

# Function for viewing the contacts:
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n" + " " * 5 + "Contact List:")
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

# Function to search for a contact by name or phone number:
def search_contacts(contacts):
    search_term = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]]
    
    if results:
        print("\n" + " " * 5 + "Search Results:")
        for index, contact in enumerate(results):
            print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

# Function for updating an existing contact:
def update_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            index = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= index < len(contacts):
                print("Leave the field empty if you do not want to update it.")
                name = input(f"Enter new name (current: {contacts[index]['name']}): ") or contacts[index]['name']
                
                phone = input(f"Enter new phone (current: {contacts[index]['phone']}): ") or contacts[index]['phone']
                while phone and not is_valid_phone(phone):
                    print("Invalid phone number. Please enter a valid phone number.")
                    phone = input("Enter new phone number: ")
                
                email = input(f"Enter new email (current: {contacts[index]['email']}): ") or contacts[index]['email']
                while email and not is_valid_email(email):
                    print("Invalid email address. Please enter a valid email.")
                    email = input("Enter new email: ")
                
                address = input(f"Enter new address (current: {contacts[index]['address']}): ") or contacts[index]['address']

                # Check for duplicate phone or email
                existing_contacts = contact_exists(contacts, phone, email)
                if existing_contacts and (contacts[index]['phone'] != phone or contacts[index]['email'] != email):
                    print("A contact with the same phone number or email already exists.")
                    for contact in existing_contacts:
                        print(f" - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                    replace = input("Do you want to replace the existing contact(s)? (yes/no): ").strip().lower()
                    if replace != 'yes':
                        print("Contact not updated.")
                        return
                    else:
                        # Replace existing contacts with the updated one
                        for contact in existing_contacts:
                            contacts.remove(contact)
                        print("Existing contact(s) replaced with the updated contact.")

                contacts[index] = {
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "address": address
                }
                save_contacts(contacts)
                print(f"Contact '{name}' updated successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= index < len(contacts):
                deleted_contact = contacts.pop(index)
                save_contacts(contacts)
                print(f"Contact '{deleted_contact['name']}' deleted successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main function to run the Smart Contact Book
def run_contact_book():
    contacts = load_contacts()
    display_welcome()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Thank you for using the Smart Contact Book. GOODBYE !!!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Start the Contact Book program
if __name__ == "__main__":
    run_contact_book()
