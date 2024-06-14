# inf117-pelakii

in order to have everything work propperly must install the python stripe library

for more documentation see included requierments document word file

Functional Modules
    main.py
        -The block comment commented-out code is the code for the address_ui.py to function as the main method of address input.
        -The code that uses JSON fine for address entry is marked in the code, is set to run using this method
        -Calc_1 is what actually creates the base calculations for tax and other information gotten from the stripe servers
        -The code following calc_1 calculates the various amounts not directly given by stripe and allows them to be saved to transactionDict. 
        -transactionDict stores all the relevant information to a transaction in the files
        -Then write transactionDict to the receipt.json file to be read by the frontend UI
        -except stripe._error.InvalidRequestError: Handles what happens when an invalid address is entered, printing an error message to the console.
JSON Files
    Checkout.json is structured as:
        {"address":
            {"line1": "", 
            "city": "", 
            "state": "", 
            "postal_code": "", 
            "country": ""}, 
        "cart": 
            [{"amount": #, 
            "tax_code": "", 
            "reference": ""}],
            // Is a list because it allows for multiple items in cart
        "shipping":#}
    Receipt.json is structured as: 
        {"item cost": #, 
        "shipping": #, 
        "subtotal": #, 
        "taxPercent": #.##, 
        "taxAmnt": #, 
        "total": #}
Testing Modules
    stripe_tax.py
        -print(stripe.tax.Settings.retrieve()): prints the current settings from the stripe tax dashboard 
        -stripe.tax.Settings.modify: Allows for modification of settings, as is set up modifies HQ address and tax code behavior
    address_ui.py : 
        The only class in this file creates and runs a UI with text entry fields for every respective field in the address dictionary. The address is stored in address_current list as ["Street Address", "City", "State", "Postal Code", "Country"]. The submit button closes the UI and allows the rest of Main.py to continue.
    createMockAddress.py
        writeToJson(): Writes a dictionary to a JSON file with the address of a WAWA in Orlando.
    printReceiptConsole.py
        The only function in this module takes in a receipt dictionary (see receipt.json) and prints it, some of the calculations for the numbers are made in main.py: 
        
        item cost: 515
        shipping: 300
        ______________________________+
        subtotal: 815
        Tax %: 6.60%
        Tax amnt: 34
        ______________________________+
        total: 849

