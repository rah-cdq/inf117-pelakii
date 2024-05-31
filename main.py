import address_ui
import stripe
import tkinter as tk
stripe.api_key = ""


if __name__ == "__main__":
  root = tk.Tk()
  app = address_ui.UserAddress(root)
  root.mainloop()

  #stripe.tax.Settings.retrieve(stripe_account='{{CONNECTED_ACCOUNT_ID}}')

  stripe.tax.Calculation.create(
    currency="usd",
    line_items=[{"amount": 1000, "reference": "L1"}],
    customer_details={
      "address": {
        "line1": app.address_current[0],
        "city": app.address_current[1],
        "state": app.address_current[2],
        "postal_code": app.address_current[3],
        "country": app.address_current[4],
      },
      "address_source": "shipping",
    },
  )
