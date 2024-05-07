import csv
import os
import shutil

def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append({'name': row[0], 'email': row[1], 'phone': row[2]})
    return contacts

def save_contacts(contacts, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow([contact['name'], contact['email'], contact['phone']])

def add_contact(contacts, name, email, phone):
    contacts = [{'name': name, 'email': email, 'phone': phone}]
    return contacts

def find_contact(contacts, name):
    if contacts:
        return contacts[0]
    else:
        return None

def remove_contact(contacts, name):
    contact = find_contact(contacts, name)
    if contact:
        contacts.remove(contact)

def update_contact(contacts, name, email, phone):
    contact = find_contact(contacts, name)
    if contact:
        contact['email'] = email
        contact['phone'] = phone

def search_contacts(contacts, query):
    results = [contact for contact in contacts if query.lower() in contact['name'].lower()]
    return results

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")

def export_contacts(contacts, filename):
    save_contacts(contacts, 'Incorrect_Contacts.csv')
    print(f"Contacts exported to {filename}")

def import_contacts(contacts, filename):
    if os.path.exists(filename):
        shutil.copy(filename, 'Sample_Contacts.csv')
        print(f"Contacts imported from {filename}")
    else:
        print("File not found.")

def main():
    filename = 'Sample_Contacts.csv'
    contacts = load_contacts(filename)

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. List All Contacts")
        print("6. Export Contacts")
        print("7. Import Contacts")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            contacts = add_contact(contacts, name, email, phone)
            save_contacts(contacts, filename)
        elif choice == '2':
            name = input("Enter name of the contact to remove: ")
            remove_contact(contacts, name)
            save_contacts(contacts, filename)
        elif choice == '3':
            name = input("Enter name of the contact to update: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone number: ")
            update_contact(contacts, name, email, phone)
            save_contacts(contacts, filename)
        elif choice == '4':
            query = input("Enter name to search: ")
            search_result = search_contacts(contacts, query)
            display_contacts(search_result)
        elif choice == '5':
            display_contacts(contacts)
        elif choice == '6':
            export_filename = input("Enter filename to export contacts: ")
            export_contacts(contacts, export_filename)
        elif choice == '7':
            import_filename = input("Enter filename to import contacts: ")
            import_contacts(contacts, import_filename)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == '__main__':
    main()
