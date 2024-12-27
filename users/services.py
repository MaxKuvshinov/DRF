import stripe

from config.settings import API_KEY_STRIPE

stripe.api_key = API_KEY_STRIPE


def create_product_stripe(course):
    """Создание продукта в Stripe"""
    product = stripe.Product.create(name=course.title, description=course.description)
    return product


def create_price_stripe(amount, product_id):
    """Создание цены на продукт в Stripe"""
    price = stripe.Price.create(
        currency="rub", unit_amount=int(amount * 100), product=product_id
    )
    return price


def create_sessions_stripe(price_id):
    """Создание сессии на оплату в Stripe"""
    sessions = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
        success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="https://example.com/cancel",
    )
    return sessions.id, sessions.url
