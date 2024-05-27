import address_ui
import stripe_tax


if __name__ == "__main__":
    userAdress = address_ui.run_address_ui()
    print(userAdress)

    stripe.tax.Calculation.create(
currency="usd",
  line_items=[{"amount": 1000, "reference": "L1"}],
  customer_details={
    "address": userAdress,
    "address_source": "shipping",
  },
)