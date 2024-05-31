import address_ui
import stripe
import tkinter as tk
stripe.api_key = ""


if __name__ == "__main__":
  root = tk.Tk()
  app = address_ui.UserAddress(root)
  root.mainloop()


  stripe.tax.Calculation.create(
  currency="usd",
  line_items=[{"amount": 1000, "reference": "L1"}],
  customer_details={
    "address": app.address_current,
    "address_source": "shipping",
  },
  )
