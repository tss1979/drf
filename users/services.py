
import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


class StripeManager:

    def create_price(self, amount, product):
        return stripe.Price.create(
            currency="rub",
            unit_amount=amount * 100,
            product_data={"name": product.name}
        )

    def create_session(self, price):
        session = stripe.checkout.Session.create(
            success_url='http://127.0.0.1:8000/',
            line_items=[{"price": price.get("id"), "quantity": 1}],
            mode="payment"
        )
        return session.get("id"), session.get("url")

    def create_product(self, course):
        return stripe.Product.create(
            name=course.title,
        )
