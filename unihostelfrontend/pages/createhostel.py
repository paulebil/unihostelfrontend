import reflex as rx
from ..templates.template import base_template

@rx.page(route="/create", title="Create Hostel")
def create_hostel() -> rx.Component:
    """Create Hostel page for the custodian."""
    return base_template(
        content=rx.container(
            rx.heading("Welcome to UniHostel", size="9"),
            rx.text("This is the Create Hostel page for custodians."),
            rx.link(rx.text("SearchHostels"), href="/search", color=rx.color("accent", 12)),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        title="Home Page",  # Pass the title dynamically
    )

