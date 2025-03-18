import reflex as rx

from ..templates.template import layout

@rx.page(route="/admin", title="Admin Page")
def admin() -> rx.Component:
    """Admin page for the app."""
    return layout(
        rx.container(
            rx.heading("Welcome to UniHostel", size="9"),
            rx.text("This is the Admin page."),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )
