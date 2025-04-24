import reflex as rx
from ..templates.template import base_template

from unihostelfrontend.components.payment_card import show_payment

@rx.page(route="/payment/make", title="Make Payment")
def make_payment() -> rx.Component:

    return base_template(
        content=rx.flex(
            rx.text("Payment Page"),
            justify="center",
            spacing="4",
        ),
    )