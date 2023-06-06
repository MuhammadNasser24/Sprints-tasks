import csv
from datetime import datetime

class ContactBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []

    def create_contact(self, username, email, phone_numbers, address):
        contact = {
            'username': username,
            'email': email,
            'phone_numbers': phone_numbers,
            'address': address,
            'insertion_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.contacts.append(contact)

    def update_contact(self, index, field, value):
        if index >= 0 and index < len(self.contacts):
            contact = self.contacts[index]
            if field in contact:
                contact[field] = value
            else:
                print("Invalid field!")
        else:
            print("Invalid index!")

    def delete_contact(self, index):
        if index >= 0 and index < len(self.contacts):
            del self.contacts[index]
        else:
            print("Invalid index!")

    def list_contacts(self):
        for index, contact in enumerate(self.contacts):
            print(f"Contact {index + 1}:")
            print(f"Username: {contact['username']}")
            print(f"Email: {contact['email']}")
            print(f"Phone Numbers: {', '.join(contact['phone_numbers'])}")
            print(f"Address: {contact['address']}")
            print(f"Insertion Date: {contact['insertion_date']}")
            print()

    def save_to_csv(self):
        with open(self.filename, 'w', newline='') as csvfile:
            fieldnames = ['username', 'email', 'phone_numbers', 'address', 'insertion_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.contacts)


# Example usage
contact_book = ContactBook("contactbook.csv")

# Create contacts
contact_book.create_contact("John Doe", "john.doe@example.com", ["1234567890"], "123 Street")
contact_book.create_contact("Jane Smith", "jane.smith@example.com", ["9876543210"], "456 Avenue")

# Update contact
contact_book.update_contact(0, "address", "456 Street")

# Delete contact
contact_book.delete_contact(1)

# List all contacts
contact_book.list_contacts()

# Save contacts to CSV file
contact_book.save_to_csv()
