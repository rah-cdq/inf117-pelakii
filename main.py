import stripe
stripe.api_key = ""
import json

#import address_ui
#import tkinter as tk
import createMockAddress
import printRecieptConsole

if __name__ == "__main__":
  #root = tk.Tk()
  #app = address_ui.UserAddress(root)
  #root.mainloop()

  #stripe.tax.Settings.retrieve(stripe_account='{{CONNECTED_ACCOUNT_ID}}')
  try:
    #createMockAddress.writeToJson

    with open('address.json', 'r') as json_file:
    
      curAddress = json.load(json_file)



    calc_1 = stripe.tax.Calculation.create(
      currency="usd",
      line_items=[
    {
      "amount": 1000,
      "tax_code": "txcd_99999999",
      "reference": "Pelakii Snack Box",
    },
  ],
  shipping_cost={"amount": 300},
  expand=["line_items"],
      customer_details={
        "address": curAddress,
        "address_source": "shipping",
      },
    )

    subtotal = calc_1.amount_total - calc_1.tax_amount_exclusive
    taxPercent = calc_1.tax_amount_exclusive/(subtotal-calc_1.shipping_cost["amount"])
    formatted_taxPercent = float("%.3f" % taxPercent)*100

    transactionDict= {
      "item cost": (subtotal-calc_1.shipping_cost["amount"]),
      "shipping": calc_1.shipping_cost["amount"],
      "subtotal":subtotal,
      "taxPercent":taxPercent,
      "taxAmnt": calc_1.tax_amount_exclusive,
      "total":calc_1.amount_total
      }
    
    printRecieptConsole.printReceipt(transactionDict)
    

    with open('receipt.json', 'w') as json_file:
        json.dump(transactionDict, json_file)

   

  except stripe._error.InvalidRequestError:
    print("Invalid Address")

