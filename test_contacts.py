import unittest
import os
import csv
from contact_management import load_contacts, save_contacts, add_contact, remove_contact, update_contact, find_contact, search_contacts

class TestContactManagement(unittest.TestCase):
    def setUp(self):
        self.contacts = [
            {'name': 'John Doe', 'email': 'john@example.com', 'phone': '1234567890'},
            {'name': 'Jane Doe', 'email': 'jane@example.com', 'phone': '0987654321'}
        ]
        self.filename = 'Sample_Contacts.csv'

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load_contacts(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['John Doe', 'john@example.com', '1234567890'])
            writer.writerow(['Jane Doe', 'jane@example.com', '0987654321'])
        loaded_contacts = load_contacts(self.filename)
        self.assertEqual(loaded_contacts, self.contacts)

    def test_save_contacts(self):
        save_contacts(self.contacts, self.filename)
        loaded_contacts = load_contacts(self.filename)
        self.assertEqual(loaded_contacts, self.contacts)

    def test_add_contact(self):
        new_contact = {'name': 'New Contact', 'email': 'new@example.com', 'phone': '5555555555'}
        add_contact(self.contacts, new_contact['name'], new_contact['email'], new_contact['phone'])
        self.assertIn(new_contact, self.contacts)

    def test_remove_contact(self):
        remove_contact(self.contacts, 'John Doe')
        self.assertNotIn({'name': 'John Doe', 'email': 'john@example.com', 'phone': '1234567890'}, self.contacts)

    def test_update_contact(self):
        update_contact(self.contacts, 'Jane Doe', 'new_email@example.com', '9999999999')
        updated_contact = {'name': 'Jane Doe', 'email': 'new_email@example.com', 'phone': '9999999999'}
        self.assertIn(updated_contact, self.contacts)

    def test_find_contact(self):
        found_contact = find_contact(self.contacts, 'John Doe')
        self.assertEqual(found_contact, {'name': 'John Doe', 'email': 'john@example.com', 'phone': '1234567890'})

    def test_find_contact_nonexistent(self):
        found_contact = find_contact(self.contacts, 'Nonexistent')
        self.assertIsNone(found_contact)

    def test_search_contacts(self):
        search_result = search_contacts(self.contacts, 'Jane')
        self.assertEqual(search_result, [{'name': 'Jane Doe', 'email': 'jane@example.com', 'phone': '0987654321'}])

if __name__ == '__main__':
    unittest.main()
