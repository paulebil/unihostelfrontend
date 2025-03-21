import reflex as rx
from ..templates.template import base_template

@rx.page(route="/", title="Home Page")
def index() -> rx.Component:
    """Home page for the app."""
    return base_template(
        content=rx.container(
            rx.heading("Welcome to UniHostel", size="9"),
            rx.text("This is the home page."),
            rx.link(rx.text("SearchHostels"), href="/search", color=rx.color("accent", 12)),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        title="Home Page",  # Pass the title dynamically
    )

