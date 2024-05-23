import stripe
import stripe_tax
stripe.api_key = ""

stripe.tax.Transaction.create_from_calculation(
  calculation="{{TAX_CALCULATION}}",
  reference='{{PAYMENT_INTENT_ID}}',
  expand=["line_items"],
)

stripe.PaymentIntent.modify(
  '{{PAYMENT_INTENT_ID}}',
  metadata={"tax_transaction": "{{TAX_TRANSACTION}}"},
)