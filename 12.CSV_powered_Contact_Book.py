import csv
import os

FILENAME = 'contacts.csv'
if not os.path.exists(FILENAME):
    with open(FILENAME,'w',newline='',encoding='utf-8') as f:
        csv.writer(f).writerow(['name','phone','email'])

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    with open(FILENAME,'a',newline='',encoding='utf-8') as f:
        csv.writer(f).writerow([name,phone,email])
    print("Contact added successfully.")