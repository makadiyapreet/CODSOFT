import tkinter as tk
from tkinter import messagebox, ttk

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.selected_contact = None

        self.window = tk.Tk()
        self.window.title("Contact Book")
        self.window.geometry("600x400")

        self.name_label = tk.Label(self.window, text="Name:", font=("Arial", 12))
        self.name_label.grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(self.window, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.country_code_label = tk.Label(self.window, text="Country Code:", font=("Arial", 12))
        self.country_code_label.grid(row=1, column=0, padx=5, pady=5)

        self.phone_code_entry = tk.Entry(self.window, width=5)
        self.phone_code_entry.grid(row=1, column=1, sticky='w', padx=5, pady=5)

        self.phone_label = tk.Label(self.window, text="Phone Number:", font=("Arial", 12))
        self.phone_label.grid(row=1, column=1, padx=5, pady=5, sticky='e')

        self.phone_entry = tk.Entry(self.window, width=25)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5, sticky='e')

        self.email_label = tk.Label(self.window, text="Email:", font=("Arial", 12))
        self.email_label.grid(row=2, column=0, padx=5, pady=5)

        self.email_entry = tk.Entry(self.window, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(self.window, text="Address:", font=("Arial", 12))
        self.address_label.grid(row=3, column=0, padx=5, pady=5)

        self.address_entry = tk.Entry(self.window, width=30)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.window, text="Add Contact", command=self.add_contact, font=("Arial", 12))
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(self.window, text="Update Contact", command=self.update_contact, font=("Arial", 12))
        self.update_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(self.window, text="View Contacts", command=self.view_contacts, font=("Arial", 12))
        self.view_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.search_label = tk.Label(self.window, text="Search:", font=("Arial", 12))
        self.search_label.grid(row=7, column=0, padx=5, pady=5)

        self.search_entry = tk.Entry(self.window, width=30)
        self.search_entry.grid(row=7, column=1, padx=5, pady=5)

        self.search_button = tk.Button(self.window, text="Search", command=self.search_contact, font=("Arial", 12))
        self.search_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self.window, text="Delete Contact", command=self.delete_contact, font=("Arial", 12))
        self.delete_button.grid(row=9, column=0, columnspan=2, pady=10)

        self.contact_table = ttk.Treeview(self.window, columns=("Name", "Phone", "Email", "Address"), show='headings')
        self.contact_table.heading("Name", text="Name")
        self.contact_table.heading("Phone", text="Phone")
        self.contact_table.heading("Email", text="Email")
        self.contact_table.heading("Address", text="Address")
        self.contact_table.column("Name", width=100)
        self.contact_table.column("Phone", width=100)
        self.contact_table.column("Email", width=150)
        self.contact_table.column("Address", width=150)
        self.contact_table.grid(row=10, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.contact_table.bind('<ButtonRelease-1>', self.select_contact)

        self.window.grid_rowconfigure(10, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

    def add_contact(self):
        name = self.name_entry.get()
        phone_code = self.phone_code_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone_number:
            full_phone = f"+{phone_code} {phone_number}"
            self.contacts[name] = {"phone": full_phone, "email": email, "address": address}
            self.clear_entries()
            self.refresh_contact_table()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def update_contact(self):
        if self.selected_contact:
            old_name = self.selected_contact
            name = self.name_entry.get()
            phone_code = self.phone_code_entry.get()
            phone_number = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if old_name in self.contacts:
                full_phone = f"+{phone_code} {phone_number}"
                self.contacts.pop(old_name)
                self.contacts[name] = {"phone": full_phone, "email": email, "address": address}
                self.clear_entries()
                self.refresh_contact_table()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showerror("Error", "Contact not found.")
        else:
            messagebox.showerror("Error", "No contact selected for update.")

    def delete_contact(self):
        if self.selected_contact:
            name = self.selected_contact

            if name in self.contacts:
                del self.contacts[name]
                self.clear_entries()
                self.refresh_contact_table()
                messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showerror("Error", "Contact not found.")
        else:
            messagebox.showerror("Error", "No contact selected for deletion.")

    def view_contacts(self):
        self.refresh_contact_table()

    def search_contact(self):
        search_term = self.search_entry.get()
        found = False
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details["phone"]:
                self.show_search_result(name, details)
                found = True
                break
        if not found:
            messagebox.showerror("Not Found", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_code_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.selected_contact = None

    def refresh_contact_table(self):
        for item in self.contact_table.get_children():
            self.contact_table.delete(item)
        for name, details in self.contacts.items():
            self.contact_table.insert('', tk.END, values=(name, details["phone"], details["email"], details["address"]))

    def show_search_result(self, name, details):
        result_text = f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}"
        messagebox.showinfo("Contact Found", result_text)

    def select_contact(self, event):
        selected_item = self.contact_table.selection()
        if selected_item:
            item = self.contact_table.item(selected_item)
            name = item['values'][0]
            details = self.contacts[name]

            self.selected_contact = name
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.phone_code_entry.delete(0, tk.END)
            self.phone_code_entry.insert(0, details['phone'].split()[0][1:])  # Extract the country code
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, ' '.join(details['phone'].split()[1:]))  # Extract the phone number
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, details['email'])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, details['address'])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()