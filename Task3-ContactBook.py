'''Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction.'''

import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_no, email, addr):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.addr = addr

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        contact_list = ""
        for index, contact in enumerate(self.contacts, start=1):
            contact_list += f"{index}. {contact.name}: {contact.phone_no}\n"
        return contact_list

    def search_contact(self, info):
        results = []
        for contact in self.contacts:
            if info.lower() in contact.name.lower() or info in contact.phone_no:
                results.append(contact)
        return results

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

class Contact_Book:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contact_manager = ContactBook()

        self.label = tk.Label(master, text="CONTACT BOOK", font=("Arial", 14, "bold"))
        self.label.grid(row=0, columnspan=2, pady=10)

        self.button_add = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=1,column=0, pady=8)

        self.button_view = tk.Button(master, text="View Contact List", command=self.view_contact_list)
        self.button_view.grid(row=2, column=0, pady=8)

        self.button_search = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.button_search.grid(row=3, column=0, pady=8)

        self.button_update = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.button_update.grid(row=4, column=0, pady=8)

        self.button_delete = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.button_delete.grid(row=5, column=0, pady=8)

        self.button_exit = tk.Button(master, text="Exit", command=self.master.destroy)
        self.button_exit.grid(row=6, column=0, pady=8 ,padx=125)

    def add_contact(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Add Contact")

        tk.Label(self.add_window, text="Name:").grid(row=0, column=0)
        self.entry_name = tk.Entry(self.add_window)
        self.entry_name.grid(row=0, column=1)

        tk.Label(self.add_window, text="Phone Number:").grid(row=1, column=0)
        self.entry_phone = tk.Entry(self.add_window)
        self.entry_phone.grid(row=1, column=1)

        tk.Label(self.add_window, text="Email:").grid(row=2, column=0)
        self.entry_email = tk.Entry(self.add_window)
        self.entry_email.grid(row=2, column=1)

        tk.Label(self.add_window, text="Address:").grid(row=3, column=0)
        self.entry_addr = tk.Entry(self.add_window)
        self.entry_addr.grid(row=3, column=1)

        tk.Button(self.add_window, text="Submit", command=self.submit_contact).grid(row=4, columnspan=2)

    def submit_contact(self):
        name = self.entry_name.get()
        phone_no = self.entry_phone.get()
        email = self.entry_email.get()
        addr = self.entry_addr.get()
        contact = Contact(name, phone_no, email, addr)
        self.contact_manager.add_contact(contact)
        messagebox.showinfo("Success", "Contact added successfully.")
        self.add_window.destroy()

    def view_contact_list(self):
        if not self.contact_manager.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            self.view_window = tk.Toplevel(self.master)
            self.view_window.title("View Contact List")
            tk.Label(self.view_window, text=self.contact_manager.view_contact_list()).pack()

    def search_contact(self):
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Search Contact")

        tk.Label(self.search_window, text="Enter name or phone number:").grid(row=0, column=0)
        self.entry_search = tk.Entry(self.search_window)
        self.entry_search.grid(row=0, column=1)
        tk.Button(self.search_window, text="Search", command=self.perform_search).grid(row=1, columnspan=2)

    def perform_search(self):
        info = self.entry_search.get()
        results = self.contact_manager.search_contact(info)
        if not results:
            messagebox.showinfo("Info", "No contacts found.")
        else:
           result_text = "\n".join([f"{i+1}. {contact.name}: {contact.phone_no}" for i, contact in enumerate(results)])
           self.result_window = tk.Toplevel(self.master)
           self.result_window.title("Search Results")
           tk.Label(self.result_window, text=result_text).pack()

    def update_contact(self):
        self.update_window = tk.Toplevel(self.master)
        self.update_window.title("Update Contact")

        tk.Label(self.update_window, text="Enter the index of contact to update:").grid(row=0, column=0)
        self.entry_index = tk.Entry(self.update_window)
        self.entry_index.grid(row=0, column=1)
        tk.Button(self.update_window, text="Get Contact", command=self.get_contact).grid(row=1, columnspan=2)

    def get_contact(self):
        index = int(self.entry_index.get())
        if index < 1 or index > len(self.contact_manager.contacts):
            messagebox.showerror("Error", "Invalid index.")
        else:
           contact = self.contact_manager.contacts[index - 1]
           self.update_window.destroy()
           self.update_form(index-1, contact)
        
    def update_form(self, index, contact):
        self.update_window = tk.Toplevel(self.master)
        self.update_window.title("Update Contact")

        tk.Label(self.update_window, text="Name:").grid(row=0, column=0)
        self.entry_name = tk.Entry(self.update_window)
        self.entry_name.insert(0, contact.name)
        self.entry_name.grid(row=0, column=1)

        tk.Label(self.update_window, text="Phone Number:").grid(row=1, column=0)
        self.entry_phone = tk.Entry(self.update_window)
        self.entry_phone.insert(0, contact.phone_no)
        self.entry_phone.grid(row=1, column=1)

        tk.Label(self.update_window, text="Email:").grid(row=2, column=0)
        self.entry_email = tk.Entry(self.update_window)
        self.entry_email.insert(0, contact.email)
        self.entry_email.grid(row=2, column=1)

        tk.Label(self.update_window, text="Address:").grid(row=3, column=0)
        self.entry_addr = tk.Entry(self.update_window)
        self.entry_addr.insert(0, contact.addr)
        self.entry_addr.grid(row=3, column=1)

        tk.Button(self.update_window, text="Submit", command=lambda: self.submit_update(index)).grid(row=4, columnspan=2)

    def submit_update(self, index):
        new_name = self.entry_name.get()
        new_phone_num = self.entry_phone.get()
        new_email = self.entry_email.get()
        new_addr = self.entry_addr.get()
        new_contact = Contact(new_name, new_phone_num, new_email, new_addr)
        self.contact_manager.update_contact(index, new_contact)
        messagebox.showinfo("Success", "Contact updated successfully.")
        self.update_window.destroy()

    def delete_contact(self):
        self.delete_window = tk.Toplevel(self.master)
        self.delete_window.title("Delete Contact")

        tk.Label(self.delete_window, text="Enter the index of contact to delete:").grid(row=0, column=0)
        self.entry_index = tk.Entry(self.delete_window)
        self.entry_index.grid(row=0, column=1)

        tk.Button(self.delete_window, text="Delete", command=self.perform_delete).grid(row=1, columnspan=2)

    def perform_delete(self):
        index = int(self.entry_index.get())
        if index < 1 or index > len(self.contact_manager.contacts):
             messagebox.showerror("Error", "Invalid index.")
        else:
            self.contact_manager.delete_contact(index - 1)
            messagebox.showinfo("Success", "Contact deleted successfully.")
            self.delete_window.destroy()

def main():
    root = tk.Tk()
    root.geometry("300x300")
    app = Contact_Book(root)
    root.mainloop()

if __name__ == "__main__":
    main()
