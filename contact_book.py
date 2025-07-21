class Contact_Book:                 ## CLASS

    def __init__(self):
        self.contacts = []          ## CONTACT LIST


    def add_contact(self):          ## ADD CONTACT

        print("     ADD CONTACT:")
        name = input("\nEnter Contact Name : ")
        phone = input("\nEnter Contact Phone Number : ")
        email = input("\nEnter Contact email : ")
        address = input("\nEnter Contact Address : ")

        individual = {'Name' : name,
                      'Phone Number' : phone,
                      'Email' : email,
                      'Address' : address}

        self.contacts.append(individual)
        print("New Contact added successfully.\n")


    
    def display_contact(self):      ## VIEW CONTACT

        if not self.contacts:
            print("Empty Contact.\n")
        else:
            print("     CONTACT LIST\n")
            print(f"INDEX    NAME    PHONE NUMBER\n")
            for i, c in enumerate(self.contacts):
                print(f" {i + 1}.    {c['Name']}    {c['Phone Number']}")
            print()
    


    def search_contact(self):       ## SEARCH CONTACT

        if not self.contacts:
            print("Empty Contact.\n")
            return
        
        print("Press 1 for search using Name or \nPress 2 for search using Phone Number:\n")
        ch = int(input("Enter here (1-2): "))
        found = False

        if ch == 1:
            s_name = input("Enter Contact Name to be searched : ")
            for i in self.contacts:
                if s_name.lower() in i['Name'].lower():
                    print("Found.\n")
                    self.display_full_contact(i)
                    found = True
                    
                
        elif ch == 2:
            s_phone = input("Enter Contact Phone Number to be searched : ")
            for i in self.contacts:
                if s_phone in i['Phone Number']:
                    print("Found.\n")
                    self.display_full_contact(i)
                    found = True    
        
        else:
            print("Invalid choice!")

        if not found:
            print("Contact not found.\n")
    


    def update_contact(self):       ## UPDATE CONTACT

        if not self.contacts:
            print("Empty Contact.\n")
            return

        s_name = input("Enter the name of the contact to update: ").strip()
        found = False

        for contact in self.contacts:
            if s_name.lower() in contact['Name'].lower():
                print("Leave field blank to keep current value.")
                new_name = input(f"New Name ({contact['Name']}): ") or contact['Name']
                new_phone = input(f"New Phone ({contact['Phone Number']}): ") or contact['Phone Number']
                new_email = input(f"New Email ({contact['Email']}): ") or contact['Email']
                new_address = input(f"New Address ({contact['Address']}): ") or contact['Address']

                contact['Name'] = new_name
                contact['Phone Number'] = new_phone
                contact['Email'] = new_email
                contact['Address'] = new_address

                print("Contact updated successfully!\n")
                found = True
                break
                


    def delete_contact(self):       ## DELETE CONTACT

        if not self.contacts:
            print("Empty Contact.\n")
            return

        s_name = input("Enter Contact Name to be deleted: ").strip()
        found = False

        for i, contact in enumerate(self.contacts):
            if s_name.lower() in contact['Name'].lower():
                confirm = input(f"Are you sure you want to delete '{contact['Name']}'? (1 for Yes / 2 for No): ")
                if confirm == '1':
                    self.contacts.pop(i)
                    print("Contact deleted successfully!\n")
                elif confirm == '2':
                    print("Deletion cancelled.\n")
                else:
                    print("Invalid input. Deletion cancelled.\n")
                found = True
                break

        if not found:
            print("Contact not found.\n")



    def display_full_contact(self, contact):    ## DISPLAY INDIVIDUAL CONTACT
        
        print("CONTACT DETAILS\n")
        for key, value in contact.items():
            print(f"{key}: {value}")
        print()



    def run(self):          ## RUN METHOD
        while True:
            print('''
==== CONTACT BOOK MENU ====
                  
1. Add Contact
2. Display Contact List
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
                  ''')
            choice = input("Enter your choice (1-6): ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.display_contact()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.\n")



if __name__ == '__main__':      ## MAIN
    c = Contact_Book()         ## OBJECT CREATION
    c.run()                    ## RUN