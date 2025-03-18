import reflex as rx

from ..templates.template import layout

@rx.page(route="/booking", title="Booking Page")
def booking() -> rx.Component:
    """Booking page for the app."""
    return layout(
        rx.container(
            rx.heading("Welcome to UniHostel", size="9"),
            rx.text("This is the Booking page."),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )
