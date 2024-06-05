import address_ui
import stripe
import tkinter as tk
stripe.api_key = ""

if __name__ == "__main__":
  root = tk.Tk()
  app = address_ui.UserAddress(root)
  root.mainloop()

  #stripe.tax.Settings.retrieve(stripe_account='{{CONNECTED_ACCOUNT_ID}}')
  try:
    stripe.tax.Settings.modify(
    defaults={"tax_code": "txcd_99999999", "tax_behavior": "inclusive"},
    head_office={"address": {"line1":"390 NE 191st St #8129","city":"Miami","state":"FL","postal_code":"33179","country": "US"}},
    )

    calc_1 = stripe.tax.Calculation.create(
      currency="usd",
      line_items=[
    {
      "amount": 1500,
      "tax_code": "txcd_99999999",
      "reference": "Pelakii Snack Box",
    },
  ],
  shipping_cost={"amount": 300},
  expand=["line_items"],
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
    print(calc_1.tax_amount_exclusive)
  except stripe._error.InvalidRequestError:
    print("Invalid Address")

