import stripe
import stripe_tax
stripe.api_key = ""

def create_checkout_session():
  try:
    checkout_session = stripe.checkout.Session.create(
      line_items = [{
        'price': '',
        'quantity': 1,
      }],
      mode = 'payment',
    )
  except Exception as e:
    return "error"
  return redirect(checkou_session.url, code=303)
