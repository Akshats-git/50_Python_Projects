import csv
import os

FILENAME = 'contacts.csv'
if not os.path.exists(FILENAME):
    with open(FILENAME,'w',newline='',encoding='utf-8') as f:
        csv.writer(f).writerow(['name','phone','email'])

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    with open(FILENAME, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['name'].lower() == name.lower():
                print("Contact with this name already exists.")
                return

    with open(FILENAME, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])

    print("Contact added successfully.")


def view_contacts():
    with open(FILENAME,'r',newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        contacts = list(reader)
        if not contacts:
            print("No contacts found.")
            return
        for i, contact in enumerate(contacts,1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    name = input("Enter name to search: ")
    with open(FILENAME,'r',newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for contact in reader:
            if contact['name'].lower() == name.lower():
                print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                return
        print("Contact not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()