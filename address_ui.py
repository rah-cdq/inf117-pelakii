import tkinter as tk
from tkinter import messagebox

# Function to handle the submission of the address
def submit_address():
    street = street_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    postal_code = postal_code_entry.get()
    country = country_entry.get()

    if street and city and state and postal_code and country:
        messagebox.showinfo("Address Submitted", 
                            f"Street Address: {street}\nCity: {city}\nState: {state}\nPostal Code: {postal_code}\nCountry: {country}")
    else:
        messagebox.showwarning("Input Error", "Please enter all parts of the address.")
    print(street)
    return [street, city, state, postal_code, country]

# Create the main application window
root = tk.Tk()
root.title("Address Input")

# Create a label and entry for each part of the address
labels = ["Street Address", "City", "State", "Postal Code", "Country"]
entries = {}

for label in labels:
    lbl = tk.Label(root, text=f"Enter {label}:")
    lbl.pack(pady=5)
    
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)
    
    entries[label] = entry

# Access the individual entries
street_entry = entries["Street Address"]
city_entry = entries["City"]
state_entry = entries["State"]
postal_code_entry = entries["Postal Code"]
country_entry = entries["Country"]

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_address)
submit_button.pack(pady=20)

# Run the application
root.mainloop()