import stripe
import stripe_tax
stripe.api_key = ""

stripe.tax.Transaction.create_from_calculation(
  calculation="{{TAX_CALCULATION}}",
  reference='{{PAYMENT_INTENT_ID}}',
  expand=["line_items"],
  "error": {
    "doc_url": "https://stripe.com/docs/error-codes/customer-tax-location-invalid",
    "code": "customer_tax_location_invalid",
    "message": "We could not determine the customer's tax location based on the provided customer address.",
    "param": "customer_details[address]",
    "type": "invalid_request_error"
  }
)

stripe.PaymentIntent.modify(
  '{{PAYMENT_INTENT_ID}}',
  metadata={"tax_transaction": "{{TAX_TRANSACTION}}"},
)

stripe.tax.customer_tax_location_invalid()
