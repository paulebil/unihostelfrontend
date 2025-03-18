import reflex as rx

from ..templates.template import layout

@rx.page(route="/", title="Home Page")
def index() -> rx.Component:
    """Home page for the app."""
    return layout(
        rx.container(
            rx.heading("Welcome to UniHostel", size="9"),
            rx.text("This is the home page."),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )

