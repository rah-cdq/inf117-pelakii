# Creates a UI to directly enter address to stripe tax, for debugging purposes

import tkinter as tk
from tkinter import messagebox

class UserAddress:
    def __init__(self, root):
        
        # Runs UI for adress entry ()
        self.root = root
        self.address_current = []
        self.root.title("Address Input")

        # Creates labels and txt entry fields for each part of the address
        labels = ["Street Address", "City", "State", "Postal Code", "Country"]
        self.entries = {}

        for label in labels:
            lbl = tk.Label(root, text=f"Enter {label}:")
            lbl.pack(pady=5)
            
            entry = tk.Entry(root, width=50)
            entry.pack(pady=5)
            
            self.entries[label] = entry

        # Allows for access to the inputs
        self.street_entry = self.entries["Street Address"]
        self.city_entry = self.entries["City"]
        self.state_entry = self.entries["State"]
        self.postal_code_entry = self.entries["Postal Code"]
        self.country_entry = self.entries["Country"]

        # Creates a submit button
        submit_button = tk.Button(root, text="Submit", command=self.submit_address)
        submit_button.pack(pady=20)

    def submit_address(self):
        self.address_current = []
        street = self.street_entry.get()
        city = self.city_entry.get()
        state = self.state_entry.get()
        postal_code = self.postal_code_entry.get()
        country = self.country_entry.get()

        if street and city and state and postal_code and country:
            messagebox.showinfo("Address Submitted", 
                                f"Street Address: {street}\nCity: {city}\nState: {state}\nPostal Code: {postal_code}\nCountry: {country}")
            self.address_current = [street, city, state, postal_code, country]
            self.root.quit()  
            # Closes the UI after submission
        else:
            messagebox.showwarning("Input Error", "Please enter all parts of the address.")
