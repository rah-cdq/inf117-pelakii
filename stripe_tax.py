
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = ""


stripe.tax.Calculation.create(
  currency="usd",
  line_items=[{"amount": 1000, "reference": "L1"}],
  customer_details={
    "address": {
      "line1": "",
      "city": "",
      "state": "",
      "postal_code": "",
      "country": "US",
    },
    "address_source": "shipping",
  },
)
