import reflex as rx

from ..templates.template import layout

@rx.page(route="/search", title="Search Page")
def search() -> rx.Component:
    """Search page for the app."""
    return layout(
        rx.container(
            rx.heading("Welcome to UniHostel", size="9"),
            rx.text("This is the search page."),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )


